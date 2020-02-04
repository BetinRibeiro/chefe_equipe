# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('PRINCIPAL'), False, URL('default', 'index'), []),
]

if auth.requires_membership('administrador'):
    _app = request.application
    response.menu += [
        (T('ADM'), False, URL('default', 'grade'), [])
    ]
# ------------------
