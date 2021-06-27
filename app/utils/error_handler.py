from app import app
import logging
from logging import Handler, FileHandler

# Ejemplo de respuesta para http response sin template
# @app.errorhandler(404)
# def not_found_error(error):
#    app.logger.warning('404 Error')
#    return f'No hay template'


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.config['LOG_FILE'] = './application.log'
    file_handler = FileHandler(app.config['LOG_FILE'])
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.error('Unhandled Exception: %s', (e))
    return f'error message: {e}'
