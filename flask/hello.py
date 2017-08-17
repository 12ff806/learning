#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager


class User(object):
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username

user1 = User(1, "Sin")
user2 = User(2, "Janus")
users = [user1, user2]


def load_user(id):
    for u in users:
        if u.userid == id:
            return u
    return None


app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    return redirect("/user/1")

    #response = make_response("<h1>This document carries a cookie!</h1>")
    #response.set_cookie("answer", "42")
    #return response

    #user_agent = request.headers.get("User-Agent")
    #return "<p>Your browser is %s</p>" % user_agent, 400


@app.route("/user/<int:id>")
def user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return "<h1>Hello, %s!</h1>" % user.username


if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()


