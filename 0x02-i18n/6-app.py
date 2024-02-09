#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Default module settings"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    Priority order: URL parameter,
    user settings, request header, default locale
    """
    login_id = request.args.get("locale", "")
    if login_id:
        return users.get(int(login_id), None)

    return None


@babel.localeselector
def get_locale() -> str:
    """Getting locale"""
    locale = request.args.get("locale", "")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    header_locale = request.headers.get("locale", "")
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request() -> None:
    """Run before any other call"""
    user = get_user()
    g.user = user


@app.route("/")
def index() -> str:
    """This is the home path"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(DEBUG=True, host="0.0.0.0", port=5000)
