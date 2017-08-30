#!/usr/bin/env python3

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    FLASKAPP_MAIL_SUBJECT_PREFIX = "[FlaskApp]"
    FLASKAPP_MAIL_SENDER = "FlaskApp Admin <Janus_Zhao@163.com>"
    FLASKAPP_ADMIN = os.environ.get("FLASKAPP_ADMIN") or "bugbugbug@protonmail.com"
    FLASKAPP_POSTS_PER_PAGE = 20
    FLASKAPP_FOLLOWERS_PER_PAGE = 50

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data.sqlite")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "data-test.sqlite")


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}


