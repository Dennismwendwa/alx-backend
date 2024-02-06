#!/usr/bin/env python3
"""This script set up flask app"""
from flask import Flask, render_template
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale() -> str:
    """Getting locale language"""
    query = request.query_string.decode("utf-8").split("&")
    query_dict = dict(map(
        lambda k: (k if "=" in k else "{}=".format(k)).split("="), query
    ))
    if "locale" in query_dict:
        if query_dict["locale"] in app.config["LANGUAGES"]:
            return query_dict["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])
# babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home() -> str:
    """This is the home page route"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
