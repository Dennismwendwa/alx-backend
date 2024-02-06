from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_timezone

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel.init_app(app)

def get_user_timezone() -> str:
    """
    Priority order: URL parameter, user settings, default to UTC
    """
    user_timezone = request.args.get('timezone', type=str)
    if user_timezone:
        try:
            get_timezone(user_timezone)
            return user_timezone
        except pytz.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            get_timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']

@babel.timezoneselector
def get_timezone() -> str:
    """Getting time zone"""
    return get_user_timezone()

@app.before_request
def before_request() -> None:
    """Runs before all calls"""
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)

@app.route('/')
def index() -> str:
    """Home route"""
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
