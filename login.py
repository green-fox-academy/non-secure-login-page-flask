from flask import Flask, render_template, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///:memory:')
table = db['logins']


@app.route("/")
def hello():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html", message="bad credentials")


if __name__ == '__main__':
    table.insert({"username": "admin", "password": "alma"})
    app.run()
