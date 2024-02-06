#!/usr/bin/env python3
"""This script set up flask app"""
from flask import Flask, render_template, g
from flask_babel import Babel, _
from typing import Union, Dic

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """mapping all supported languages"""
    LANGUAGES = [
        "en", "fr"
    ]
    BABEL_DEFAULT_LOCALE = "en"
    BALEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Getting users"""
    logged = request.args.get("login_as")
    if logged:
        return users.get(int(logged))
    return None


@app.before_request
def before_request() -> None:
    """This method runs before every other call"""
    user = get_user()
    g.user = user


def get_locale() -> str:
    """Getiing locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home() -> str:
    title = _("Welcome to Helberton")
    header = _("Hello world")

    return render_template("5-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
