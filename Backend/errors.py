class InternalServerError(Exception):
    pass

errors = {
    "InternalServerError" : {
        "message" : "Sorry! Something went wrong",
        "status" : 500
    }
}
