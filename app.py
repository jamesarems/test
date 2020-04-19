#!/usr/bin/env  python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Deployment is working"

if __name__ == '__main__':
    app.run(debug=True, port='8080')
