from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import BadRequest


def error_response(status_code, message=None):
    print('StatusCode')
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    return response, status_code


def bad_request(message):
    return error_response(400, message)


def bad_request_schema(error):
    data = BadRequest(error, None).get_description()
    data = data.split('<br>')
    datafield = data[5].replace(':', '')
    datafield = data[5].replace('On instance', '')
    data = data[0].replace('<p>400 Bad Request: ', '')
    message = f'Error {data} campo {datafield}'
    return error_response(400, message)


def non_autorhize(message):
    return error_response(401, message)

def not_found(message):
    return error_response(404, message)

def not_acceptable(message):
    return error_response(406, message)

def error_transacction(message):
    print(message)
    return error_response(500, message)


def success_request(response):
    response = jsonify(response)
    return response, 200
