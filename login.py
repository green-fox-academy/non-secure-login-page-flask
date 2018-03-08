from flask import Flask, render_template, request
import dataset
import hashlib

app = Flask(__name__)
db = dataset.connect('sqlite:///:memory:')
table = db['logins']


@app.route("/")
def hello():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    credentials = request.form.to_dict()
    return success(credentials["username"]) if validate(credentials) else bad_credentials()


def success(username):
    return render_template("success.html", username=username)


def bad_credentials():
    return render_template("login.html", message="bad credentials")


def validate(credentials):
    return get_hash(credentials["password"]) == get_password(credentials["username"])


def get_password(name):
    user = table.find_one(username=name)
    return user["password"] if user else False


def get_hash(key):
    return hashlib.md5(key.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    table.insert(
        {"username": "admin", "password": "ebbc3c26a34b609dc46f5c3378f96e08"})
    app.run()
