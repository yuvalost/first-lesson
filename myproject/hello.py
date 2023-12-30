from flask import Flask

app = flask(__name__)

@app.route("/")
def hello_workd():
    return "<p>hello, world!</p>"