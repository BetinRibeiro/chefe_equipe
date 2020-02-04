# -*- coding: utf-8 -*-
# tente algo como
def acesso_carrada():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.carrada.projeto == request.args(0, cast=int)).select(orderby=db.carrada.data_carrada)
    return locals()
@auth.requires_membership('operador')
def criar_carrada():
    projeto = db.projeto(request.args(0, auth.user))
    
    db.carrada.projeto.default = projeto.id
    db.carrada.projeto.writable = False

    form = SQLFORM(db.carrada).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_carrada', args=projeto.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_carrada():
    carrada = db.carrada(request.args(0, cast=int))
    projeto = db.projeto(carrada.projeto)
    db.carrada.id.readable = False
    db.carrada.id.writable = False
    
    db.carrada.projeto.readable = False
    db.carrada.projeto.writable = False

    form = SQLFORM(db.carrada, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_carrada', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def acesso_mercadoria():
    carrada = db.carrada(request.args(0, cast=int))
    rows = db(db.mercadoria.carrada == request.args(0, cast=int)).select(orderby=~db.mercadoria.quant_pcs_enviada)
    return locals()

@auth.requires_membership('operador')
def criar_mercadoria():
    carrada = db.carrada(request.args(0, auth.user))
    
    db.mercadoria.carrada.default = carrada.id
    db.mercadoria.carrada.writable = False

    form = SQLFORM(db.mercadoria).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_mercadoria', args=carrada.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_mercadoria():
    mercadoria = db.mercadoria(request.args(0, cast=int))
    carrada = db.carrada(mercadoria.carrada)
    db.mercadoria.id.readable = False
    db.mercadoria.id.writable = False
    
    db.mercadoria.carrada.readable = False
    db.mercadoria.carrada.writable = False

    form = SQLFORM(db.mercadoria, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_mercadoria', args=carrada.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
