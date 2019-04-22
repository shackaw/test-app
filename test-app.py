#!/usr/bin/env python
import json
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello(**kwargs):
    return "It works!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5080))
    app.run(host='0.0.0.0', port=port)