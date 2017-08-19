#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from datetime import datetime
from threading import Thread
from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask import make_response
from flask import abort
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.163.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["FLASKAPP_MAIL_SUBJECT_PREFIX"] = "[FlaskApp]"
app.config["FLASKAPP_MAIL_SENDER"] = "FlaskApp Admin <Janus_Zhao@163.com>"
app.config["FLASKAPP_ADMIN"] = os.environ.get("FLASKAPP_ADMIN")

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config["FLASKAPP_MAIL_SUBJECT_PREFIX"] + subject,
                  sender=app.config["FLASKAPP_MAIL_SENDER"], recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr


#def send_mail(to, subject, template, **kwargs):
#    msg = Message(app.config["FLASKAPP_MAIL_SUBJECT_PREFIX"] + subject,
#                  sender=app.config["FLASKAPP_MAIL_SENDER"], recipients=[to])
#    msg.body = render_template(template + ".txt", **kwargs)
#    msg.html = render_template(template + ".html", **kwargs)
#    mail.send(msg)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    sex = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User %r>" % self.username


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField("Submit")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
            if app.config["FLASKAPP_ADMIN"]:
                send_mail(app.config["FLASKAPP_ADMIN"], "New User", "mail/new_user", user=user)
        else:
            session["known"] = True
        session["name"] = form.name.data
        form.name.data = ""
        return redirect(url_for("index"))
    return render_template("index.html",
        form=form, name=session.get("name"),
        know = session.get("known", False), current_time=datetime.utcnow())
    
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


@app.route("/user/<int:id>")
def user(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        abort(404)
    return render_template("user.html", name=user.username)


if __name__ == "__main__":
    #app.run(debug=True)
    db.create_all()
    manager.run()


