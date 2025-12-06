from flask import render_template, redirect, url_for, request
from app import app
import json
from flask import session, flash


class IndexController:

    @app.route("/", methods = ['GET'])  
    def index():

        metadata = {"title": "", "pagename": "index"}

        # permet d'utiliser le template jinja "index.html" 
        # avec les données data dans la variable data (ce nom sera alors utilisé dans le template)
        return render_template('index.html', metadata = metadata)


    


    



