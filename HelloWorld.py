
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "#GGMU#ManUTD"
=======
    return "Boo!"
>>>>>>> 9e38e99cffe5d4c29b1c9f32710e7fedbe9ef087

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

