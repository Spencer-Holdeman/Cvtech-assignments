from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Password1'

    from templates import Templates

    app.register_blueprint(Templates, url_prefix='/')

    return app