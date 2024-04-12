#!/usr/bin/env python3
"""A simple flask application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """function to render a template"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
