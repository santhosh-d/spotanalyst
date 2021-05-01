import os
from flask import Flask
from flask.templating import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello Darkness!!"

@app.route('/hello')
def guide():
    return "Ok u Know ur commands"


if __name__ == '__main__':
    app.run(debug=True,host="localhost", port=9000)