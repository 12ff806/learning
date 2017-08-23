# -*- coding: utf-8 -*-


#from flask import request
#from flask import make_response
#from flask import flash

from datetime import datetime
from flask import render_template, session, redirect, abort, url_for, current_app
from flask import flash
from flask_login import current_user, login_required
from .. import db
from ..models import User, Role
from ..email import send_mail
from . import main
from .forms import NameForm, EditProfileForm, EditProfileAdminForm
from ..decorators import admin_required


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


@main.route("/user/<username>")
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template("user.html", user=user)


@main.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        flash("Your profile has been updated.")
        return redirect(url_for("main.user", username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template("edit_profile.html", form=form)


@main.route("/edit-profile/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        #db.session.commit()
        flash("The profile has been updated.")
        return redirect(url_for("main.user", username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template("edit_profile.html", form=form, user=user)


