#!/usr/bin/env  python3

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    host = os.popen('hostname').read().strip()
    return render_template('index.html', host=host)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
