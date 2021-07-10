# 기존의 우리가 app.py로 사용하던 파일을 실행시키는 파일
# 우리가 만드는 flask앱을 모듈화 시킨이후에 실행시키기 위해 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config.from_pyfile('config.py')
db=SQLAlchemy(app)

from web import routes


