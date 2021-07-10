from web import app

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY='thisisfirstflaskapp'
SQLALCHEMY_DATABASE_URI='postgresql://postgres:1111@localhost/video'

FLASK_APP = '__init__.py'