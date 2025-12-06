from flask import render_template, redirect, url_for, request
from app import app
import json

from flask import session

class HoneyController:

    @app.route("/honeycomb", methods = ['GET', 'POST'])
    def honeycomb():

        if (request.method == 'POST'):
            pass
            
        metadata = {"title": "Honeycomb", "pagename": "Honeycomb Visualization"}
        
        # if (session["progression"] == None):
        #     session["progression"] = {
        #         '1': False,
        #         '2': False,
        #         '3': False,
        #         '4': False,
        #         '5': False,
        #         '6': False,
        #         '7': False,
        #         '8': False,
        #         '9': False,
        #         '10': False,
        #         '11': False,
        #         '12': False,
        #         '13': False,
        #         '14': False,
        #         '15': False,
        #         '16': False,
        #         '17': False,
        #         '18': False,
        #         '19': False,
        #         '20': False,
        #     } 

        # permet d'utiliser le template jinja "honeycomb.html" 
        # avec les données data dans la variable data (ce nom sera alors utilisé dans le template)
        return render_template('honeycomb.html', metadata = metadata)


    @app.route("/bee_messenger", methods = ['GET'])
    def bee_messenger():
        metadata = {"title": "L'Abeille Messagère", "pagename": "bee_messenger"}
        return render_template('bee_messenger.html', metadata = metadata)


    @app.route("/chiant", methods = ['GET'])
    def chiant():
        metadata = {"title": "Attrape l'abeille", "pagename": "Jeu de l'abeille"}
        return render_template('chiant.html', metadata = metadata)


    


    



