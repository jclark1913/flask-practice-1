from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    html = "welcome"
    return html

@app.get('/welcome/home')
def welcome_home():
    html = "welcome home"
    return html

@app.get('/welcome/back')
def welcome_back():
    return "welcome back"