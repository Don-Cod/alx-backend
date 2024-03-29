#!/usr/bin/env python3
"""Basic_Babel_setup."""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class for Babel object."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """GET /
    Return: 1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
