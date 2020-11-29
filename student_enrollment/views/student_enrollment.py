from flask import (
    Blueprint,
    Response,
    request,
    make_response
)


app = Blueprint('student_enrollment', __name__)
