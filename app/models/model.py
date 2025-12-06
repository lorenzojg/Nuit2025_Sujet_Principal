import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "../static/data/fake_or_real_news.csv")
data = pd.read_csv(csv_path,encoding='utf-8', on_bad_lines='skip')
data["label_num"] = data["label"].map({"REAL": 1, "FAKE": 0})
data = data.drop_duplicates(subset=["title", "text"])

#X = titre + texte (séparés)
X = data[["title", "text"]]

#y = label numérique
y = data["label_num"].astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

text_features = ColumnTransformer(
    transformers=[
        ("title_tfidf", TfidfVectorizer(
            max_features=5000,
            ngram_range=(1, 2)
        ), "title"),
        ("text_tfidf", TfidfVectorizer(
            max_features=20000,
            ngram_range=(1, 2)
        ), "text"),
    ],
    remainder="drop"
)

logreg_pipeline = Pipeline([
    ("features", text_features),
    ("clf", LogisticRegression(
        max_iter=1000,
        n_jobs=-1
    ))
])# Entraînement
logreg_pipeline.fit(X_train, y_train)

#Prédictions
y_pred = logreg_pipeline.predict(X_test) 
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import make_scorer, f1_score

#Validation croisée stratifiée
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

#F1 pour la classe FAKE (tu as encodé FAKE = 0, REAL = 1)
f1_fake_scorer = make_scorer(f1_score, pos_label=0)

#--- CV F1 (classe FAKE=0) ---
scores_f1_fake = cross_val_score(
    logreg_pipeline,
    X_train,
    y_train,
    cv=cv,
    scoring=f1_fake_scorer,
    n_jobs=-1
)

#--- CV Accuracy ---
scores_acc = cross_val_score(
    logreg_pipeline,
    X_train,
    y_train,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix

#(Tu as déjà fait y_pred = logreg_pipeline.predict(X_test))
acc      = accuracy_score(y_test, y_pred)
f1_fake  = f1_score(y_test, y_pred, pos_label=0)  # FAKE
f1_real  = f1_score(y_test, y_pred, pos_label=1)  # REAL

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

import pandas as pd

def tester_article(title, text, model):
    # Construire un mini DataFrame comme pendant l'entraînement
    X_new = pd.DataFrame({
        "title": [title],
        "text": [text]
    })

#Prédiction
    y_pred = model.predict(X_new)[0]

#Probabilité (si dispo)
    try:
        proba = model.predict_proba(X_new)[0]
        proba_fake = proba[0]   # classe 0 = FAKE
        proba_real = proba[1]   # classe 1 = REAL
    except AttributeError:
        proba_fake = proba_real = None

    label_str = "REAL (vrai article)" if y_pred == 1 else "FAKE (article douteux)"

    print("Titre :", title[:120], "...")
    print("→ Prédiction :", label_str)
    if proba_fake is not None:
        print(f"   Probabilité FAKE : {proba_fake:.3f}")
        print(f"   Probabilité REAL : {proba_real:.3f}")

    return y_pred 
 
joblib.dump(logreg_pipeline, "app/models/model.pkl")