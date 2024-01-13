import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
		or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
notes:

flask docs on sessions: https://flask.palletsprojects.com/en/2.2.x/api/#sessions
DigitalOcean on webforms and secret keys: https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application#step-3-handling-form-requests
setting a db engine other than sqlite: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application#step-2-setting-up-the-database-and-model
configuration settings for sql alchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
how to set a secret key:
(for Windows, use set instead of export):

"""