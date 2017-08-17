#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class User(object):
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username


user1 = User(1, "Sin")
user2 = User(2, "Janus")
user3 = User(3, "ahaSin")
users = [user1, user2, user3]


def load_user(id):
    for u in users:
        if u.userid == id:
            return u
    return None


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow()) 

    #return redirect("/user/1")

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
    return render_template("user.html", name=user.username)


if __name__ == "__main__":
    #app.run(debug=True)
    manager.run()


