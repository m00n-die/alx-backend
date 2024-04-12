#!/usr/bin/env python3
"""A simple flask application"""

from flask import Flask, render_template, g, request
from flask_babel import Babel


class Config():
    """Basic config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine best language match"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def hello_world():
    """returns index.html file"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
