from sqlalchemy.sql import text
from flask import request, jsonify
from flask_cors import cross_origin
from app import app, db_pgl
from app.utils.response import bad_request, bad_request_schema, non_autorhize


# Se agrega auth
from app.middlewares.auth_freelanders import AuthFreelanders

# Modulo para validacion de schema de datos
from flask_expects_json import expects_json

EXAMPLESCHEMA = ExampleSchema()


schema_example = EXAMPLESCHEMA.schema_example()

class Application:
    @expects_json(schema_brief, force=True)
    @app.errorhandler(400)
    def error_400(error):
        try:
            return bad_request_schema(error)
        except Exception as e:
            print(e)
    
    @app.route('/')
    @app.route('/index')
    def index():
        return 'Example Backend'
    
    @app.route("/example/<param>", methods=["POST"])
    @expects_json(schema_example, force=True)
    @cross_origin()
    def update_brief(param):
        valid = AuthFreelanders.verify_token(request.headers.get("Authorization"))
        if valid is False:
            return non_autorhize("Token is required")
        data = request.get_json()
        pass
