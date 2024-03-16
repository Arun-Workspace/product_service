from flask import jsonify,Blueprint

dummy_module = Blueprint('dummy_module', __name__,url_prefix='/dummy')


@dummy_module.route('/', methods=['GET'])
def dummy(**kwargs):
    return jsonify({"message": "success"})
