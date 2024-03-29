#!/usr/bin/env python3
"""This script set up flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False


class Config:
    """mapping all supported languages"""
    LANGUAGES = [
        "en", "fr"
    ]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home() -> str:
    """Home page route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
