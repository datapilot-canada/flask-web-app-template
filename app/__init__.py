import flask
import logging
import secrets

from flask import render_template
from config import Config
from werkzeug.middleware.proxy_fix import ProxyFix

""" State Management and Login. """
# from flask_login import LoginManager, current_user, login_required
# from redis import StrictRedis
# from flask_session import Session

# login_manager = LoginManager()
# login_manager.init_app(app)
# Session(app)

# """ Setup the Redis Cache Connection."""
# redis_connection = StrictRedis(host=app.config['REDIS_CACHE_HOSTNAME'], port=6380, password=app.config['REDIS_CACHE_PASSWORD'], ssl=app.config['REDIS_CACHE_SSL'])
# app.redis = redis_connection


# """ Set additional Envirnment Variables used for CRON Jobs."""
# os.environ['REDIS_CACHE_PORT']      = str(app.config['REDIS_CACHE_PORT'])
# os.environ['REDIS_CACHE_HOSTNAME']  = app.config['REDIS_CACHE_HOSTNAME']
# os.environ['REDIS_CACHE_PASSWORD']  = app.config['REDIS_CACHE_PASSWORD']
# os.environ['REDIS_CACHE_SSL']       = str(app.config['REDIS_CACHE_SSL'])
# os.environ['APP_BASE_DIR']          = app.config['APP_BASE_DIR']

logger = logging.getLogger(__name__)

""" Create the Flask app """
app = flask.Flask(__name__)


""" Load the configuration from the Config class """
app.config.from_object(Config)


""" Setup the Flask app """
app.secret_key = secrets.token_hex()
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1 ,x_proto=1)


# """ Register the Blueprints"""
# from app.google_login import bp as login_bp
# app.register_blueprint(login_bp)


""" Setup the Routes."""
@app.route('/')
def home():
  return render_template('index.html')
