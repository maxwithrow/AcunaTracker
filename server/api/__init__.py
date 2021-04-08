from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    from api.stats import stats
    app.register_blueprint(stats, url_prefix='/stats')

    return app

