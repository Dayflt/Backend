from web import app
PORT= '5432'
USERNAME = 'postgres'
PASSWORD = '1111'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY='thisisfirstflaskapp'
SQLALCHEMY_DATABASE_URI='postgresql://' + USERNAME + ':' + PASSWORD + '@localhost:+' + PORT + '/video'
SQLALCHEMY_DATABASE_URI='postgresql://%s:%s@localhost:%s/video'%(USERNAME,PASSWORD,PORT)

FLASK_APP = '__init__.py'