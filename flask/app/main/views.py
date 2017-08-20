# -*- coding: utf-8 -*-


#from flask import request
#from flask import make_response
#from flask import flash

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from flask import abort
from .. import db
from ..models import User
from ..email import send_mail
from . import main
from .forms import NameForm


@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
            if current_app.config["FLASKAPP_ADMIN"]:
                send_mail(current_app.config["FLASKAPP_ADMIN"], "New User",
                          "mail/new_user", user=user)
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for(".index"))
    return render_template("index.html",
                           form=form, name=session.get("name"),
                           know = session.get("known", False),
                           current_time=datetime.utcnow())
    
    #form = NameForm()
    #if form.validate_on_submit():
    #    old_name = session.get("name")
    #    if old_name is not None and old_name != form.name.data:
    #        flash("Looks like you have changed your name!")
    #    session["name"] = form.name.data
    #    return redirect(url_for("index"))
    #return render_template("index.html",
    #    form=form, name=session.get("name"), current_time=datetime.utcnow()) 

    #return redirect("/user/1")

    #response = make_response("<h1>This document carries a cookie!</h1>")
    #response.set_cookie("answer", "42")
    #return response

    #user_agent = request.headers.get("User-Agent")
    #return "<p>Your browser is %s</p>" % user_agent, 400


@main.route("/user/<int:id>")
def user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        abort(404)
    return render_template("user.html", name=user.username)


