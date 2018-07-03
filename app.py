# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route("/test", methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return "Get request successful"
    elif request.method == 'POST':
        return "Post request successful"

if __name__ == '__main__':
    app.debug = True
    app.run()
