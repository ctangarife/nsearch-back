from flask import request, jsonify
from flask_cors import cross_origin
from app import app, db_pgl
from app.utils.response import bad_request, bad_request_schema, non_autorhize

from app.controllers.nsearchCategory import nsearchCategory

NSEARCH = nsearchCategory()


class Application:   
    @app.route('/')
    @app.route('/index')
    def index():
        return 'Nsearch Index plain'
    
    @app.route("/nsearch/category", methods=["GET"])
    @cross_origin()
    def categories():
        print('Entra aca 1 ')
        return NSEARCH.get_categories()
    
    @app.route("/nsearch/category/<category>", methods=["GET"])
    @cross_origin()
    def category_modules(category):
        print(category,'Entra aca module1')
        return NSEARCH.get_modules_from_category(category)

