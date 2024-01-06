from flask import Flask
app = Flask("Test")
@app.route("/")
def home():
    return "Hello, Flask!"

app.run()