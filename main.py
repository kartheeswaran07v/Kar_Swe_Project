from flask import Flask, request, render_template, url_for
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = "xxxxxxxx"


@app.route('/', methods=["GET", "POST"])
def hb_swe():
    return render_template("hb_swe.html")


@app.route('/wish', methods=["GET", "POST"])
def wish():
    return render_template("wish.html")


@app.route('/hobbies', methods=["GET", "POST"])
def hobbies():
    return render_template("hobbies.html")


@app.route('/home', methods=["GET", "POST"])
def home():
    response = requests.get("https://api.npoint.io/7a4e62f070de74e2dace")
    quote_data = response.json()
    return render_template("index.html", quotes=quote_data)


@app.route('/24')
def parallax():
    response = requests.get("https://api.npoint.io/f45b3e0d75b04a3b21c7")
    data = response.json()
    return render_template("parallax.html", contents=data)


if __name__ == "__main__":
    app.run(debug=True)

