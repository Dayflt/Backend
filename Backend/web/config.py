from web import app

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY='thisisfirstflaskapp'
SQLALCHEMY_DATABASE_URI='postgresql://postgres:sylucy12@localhost:5433/video'

FLASK_APP = '__init__.py'