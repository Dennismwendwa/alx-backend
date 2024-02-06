#!/usr/bin/env python3
"""This script set up flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)

class Config:
    """mapping all supported languages"""
    LANGUAGES = [
        "en", "fr"
    ]

app.config.from_object(Config)
babel.init_app(app)


@app.route("/")
def home() -> str:
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
