
"""Main application and routing logic for TwitOff."""
from flask import Flask, render_template
from twistoff.models import DB, User

from os import getenv
from dotenv import load_dotenv

load_dotenv()
#print(getenv('TWITTER_CONSUMER_KEY'))


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = getenv('FLASK_ENV')
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html',title='Home',users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    return app

