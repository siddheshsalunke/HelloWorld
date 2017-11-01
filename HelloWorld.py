
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():

    return "You are gonna edit me :( Pipeline works fine though! test it"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

