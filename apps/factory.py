from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from apps.dummy_module.controller import dummy_module
    app.register_blueprint(dummy_module)

    return app