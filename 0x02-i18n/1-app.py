#!/usr/bin/env python3
"""A simple flask application"""

from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Basic config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def hello_world():
    """returns index.html file"""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()
