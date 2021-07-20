from web import app
PORT= '5432'
USERNAME = 'postgres'
PASSWORD = '1111'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY='thisisfirstflaskapp'
SQLALCHEMY_DATABASE_URI='postgresql://%s:%s@localhost:%s/video'%(USERNAME,PASSWORD,PORT)


test_db = {
    'user' : 'test',
    'password' : '1111',
    'port' : '5432'
}

test_config = {
    'DB_URL' : 'postgresql://%s:%s@localhost:%s/video'%(test_db['user'], test_db['password'], test_db['port'])

}
FLASK_APP = '__init__.py'