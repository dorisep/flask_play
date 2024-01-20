from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

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