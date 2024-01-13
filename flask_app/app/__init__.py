from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

'''
on app factories in flask: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
on Flask debugger: https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application

set variables:
export FLASK_APP=app
export FLASK_ENV=development
flask run
'''