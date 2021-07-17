class InternalServerError(Exception):
    pass

errors = {
    "InternalServerError" : {
        "message" : "Sorry! Something went wrong",
        "status" : 500
    }
}

from flask import jsonify
class API_model_id(Exception):
    pass

def error2(e):
    return jsonify({
        "success":False,
        "message":"문발생"
    })