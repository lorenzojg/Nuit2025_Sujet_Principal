from flask import render_template, redirect, url_for, request
from app import app

"""
Controller for informational articles on various topics.

Routes:
- /infos/digitalSobriety
- /infos/confidentiality
- /infos/freeware
"""

class InfosController:

    @app.route('/infos/digitalSobriety', methods = ['GET'])
    def digitalSobriety():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('digitalSobriety.html', metadata=metadata, article=article)  


    @app.route('/infos/confidentiality', methods = ['GET'])
    def confidentiality():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('confidentiality.html', metadata=metadata, article=article)  

    # Logiciel gratuit
    @app.route('/infos/freeware', methods = ['GET'])
    def freeware():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('freeware.html', metadata=metadata, article=article)  

    # Logiciel libre
    @app.route('/infos/free_software', methods = ['GET']) 
    def free_software():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('free_software.html', metadata=metadata, article=article)

    @app.route('/infos/collaboration', methods = ['GET']) 
    def collaboration():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('collaboration.html', metadata=metadata, article=article)

    
    @app.route('/infos/recycling', methods = ['GET']) 
    def recycling():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('recycling.html', metadata=metadata, article=article)

    

    @app.route('/infos/planned_obsolescence', methods = ['GET']) 
    def planned_obsolescence():
        metadata = {"title": "Article", "pagename": "article"}
        
        article = {
            "title": "La vie fascinante des abeilles dans la ruche",
            "lead": "Plongez au cœur d'une ruche pour découvrir l'organisation sociale complexe et l'importance cruciale des abeilles dans notre écosystème.",
            "image": "/static/img/pokemons/bee.jpg",
            "image_alt": "Abeilles sur un rayon de miel",
            "image_caption": "Les abeilles travaillent ensemble pour construire et maintenir la ruche",
        }
        
        return render_template('planned_obsolescence.html', metadata=metadata, article=article)

    






