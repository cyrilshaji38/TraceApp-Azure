from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the Trace App! We will help you sort out your product reviews."
