#Simple Flask application

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')
def index():
    return "Welcome to the index page"










if __name__=='__main__':
    app.run(debug=True)

