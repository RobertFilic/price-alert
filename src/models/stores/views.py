from flask import Blueprint

store_blueprint = Blueprint('stores', __name__, template_folder='templates')

@store_blueprint.route('/store/<string:name>')
def store_page():
    pass