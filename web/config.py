from web import app
PORT= '5433'
USERNAME = 'postgres'
PASSWORD = 'sylucy12'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY='thisisfirstflaskapp'
SQLALCHEMY_DATABASE_URI='postgresql://%s:%s@localhost:%s/video'%(USERNAME,PASSWORD,PORT)

FLASK_APP = '__init__.py'