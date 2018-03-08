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
    return success("dwa") if validate(request.form) else bad_credentials()


def success(username):
    return render_template("success.html", username=username)


def bad_credentials():
    return render_template("login.html", message="bad credentials")


def validate(credentials):
    return True


if __name__ == '__main__':
    table.insert({"username": "admin", "password": "alma"})
    app.run()
