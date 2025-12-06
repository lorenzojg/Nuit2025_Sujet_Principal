# from flask import render_template, redirect, url_for, request,jsonify
# from app import app
# import joblib as jl
# from app.services.IAService import IAService


# iaservice = IAService()

    
# @app.route("/chat")
# def chat():
#         return render_template('userChat.html')

# @app.route("/predict",methods=['POST'])
# def predict():
#     title = request.form.get('title', '').strip()
#     text = request.form.get('text', '').strip()
#     data = None
#     if title and text:
#         data = iaservice.predict_text(title, text)
#     return render_template('userChat.html', data=data, metadata={'title' : 'chatIA', 'pagename' : 'Chat with IA'})
    
    
