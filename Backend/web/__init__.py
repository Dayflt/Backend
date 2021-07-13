# 기존의 우리가 app.py로 사용하던 파일을 실행시키는 파일
# 우리가 만드는 flask앱을 모듈화 시킨이후에 실행시키기 위해 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import errors as errors
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app, errors = errors)
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)

SWAGGER_URL='/swagger'
API_URL='/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "DAYFLY-Flask-REST-MIXEDVIDEO"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

from web import routes


