class InternalServerError(Exception):
    pass

errors = {
    "InternalServerError" : {
        "message" : "Sorry! Something went wrong",
        "status" : 500
    }
}

from web import app
from flask import jsonify

class API_model_id(Exception):
    pass
@app.errorhandler(500)
def error(e):
    return jsonify({
        "success":False,
        "message":"Something wrong"
    })
@app.errorhandler(API_model_id)
def error2(e):
    return jsonify({
        "success":False,
        "message":"문제 발생"
    })