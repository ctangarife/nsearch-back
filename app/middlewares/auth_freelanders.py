import datetime
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.wrappers import Request, Response, ResponseStream
from app import app
from app.utils.utils import jwt_encode, str_to_bool, jwt_decode

# from app.controllers.Menu import MenuController

# MENU = MenuController()


class AuthFreelanders:
    def generate_token(data):
        # respM = MENU.list_menu_fields_role(data.role.alias)
        try:
            clients = []
            for client in data.clients:
                clients.append(client.id_client)
            payload = {
                'id': data.id,
                'username': data.username,
                'role': data.role.alias,
                'agency': data.id_agency,
                'clients': clients,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60 * 5),
                'iat': datetime.datetime.utcnow(),
                #'menu': respM[0]['menu']
            }
            return jwt_encode(payload, app.config['SECRET_KEY'])

        except Exception as e:
            return e

    def verify_token(key):
        if key is None:
            return False
        key = key.split(' ')
        if len(key) != 2:
            return False
        if key[0].lower() != 'bearer':
            return False
        try:
            token = key[1]
            token = jwt_decode(token, app.config['SECRET_KEY'])
            return token
        except Exception as e:
            print(e, 'Esset es')
            return False
