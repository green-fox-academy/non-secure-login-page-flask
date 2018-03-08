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
    credentials = request.form.to_dict()
    return success(credentials["username"]) if validate(credentials) else bad_credentials()


def success(username):
    return render_template("success.html", username=username)


def bad_credentials():
    return render_template("login.html", message="bad credentials")


def validate(credentials):
    return credentials["password"] == get_password(credentials["username"])


def get_password(name):
    user = table.find_one(username=name)
    return user["password"] if user else False

if __name__ == '__main__':
    table.insert({"username": "admin", "password": "alma"})
    app.run()
