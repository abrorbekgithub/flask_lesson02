import requests
from flask import Flask
from pprint import pprint
from tinydb import TinyDB,Query

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"

@app.route('/index')
def index():
    return "index"

@app.route('/home')
def home():
    return "home page"

if __name__=="__main__":
    app.run(debug=True)