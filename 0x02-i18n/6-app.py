from flask import Flask, render_template, request, g
from flask_babel import Babel, _

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


def get_user_locale() -> str:
    """
    Priority order: URL parameter,
    user settings, request header, default locale
    """
    user_locale = request.args.get('locale', type=str)
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale

    if g.user and g.user.get('locale'
                             ) and g.user['locale'
                                          ] in app.config['LANGUAGES']:
        return g.user['locale']

    request_locale = request.headers.get('Accept-Language', '')
    if request_locale:
        return request_locale.split(',')[0]

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.localeselector
def get_locale() -> str:
    """Getting locale"""
    return get_user_locale()


@app.before_request
def before_request() -> None:
    """Run before any other call"""
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)


@app.route('/')
def index() -> str:
    """This is the home path"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
