import joblib
import os
from app.models.model import tester_article

class IAService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        model_path = os.path.join(base_dir, "models", "model.pkl")

        self.model = joblib.load(model_path)
    
    def predict_text(self, title, text) :
        if not title:
            title = ""
        if not text:
            text = ""
        return tester_article(title, text, self.model)