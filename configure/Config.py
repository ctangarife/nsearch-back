import os
BASE_DIR = os.path.abspath(os.getcwd())
class Config(object):
    # Define the database - we are working with
    # We connect with the help of the PostgreSQL URL

    user = os.environ.get('DB_USER') or 'postgres'
    password = os.environ.get('DB_PASS') or 'password'
    db = os.environ.get('DB_NAME') or 'postgres'
    host = os.environ.get('DB_HOST') or '127.0.0.1'
    port = os.environ.get('DB_PORT') or '5432'
    url = 'postgresql://{}:{}@{}:{}/{}'
    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = url.format(user, password, host, port, db)
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2
    # Statement for enabling the development environment
    DEBUG = os.environ.get('FLASK_DEBUG') or True
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = 'secret'

    # Secret key for signing JWT
    SECRET_KEY = '$LlaveSecreta$'

    CORS_HEADERS = 'Content-Type'


