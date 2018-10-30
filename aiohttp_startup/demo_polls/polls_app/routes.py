#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from views import index


def setup_routes(app):
    app.router.add_get("/", index)
