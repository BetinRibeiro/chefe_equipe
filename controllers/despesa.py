# -*- coding: utf-8 -*-
# tente algo como
def acesso_class_despesa():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.class_desp.projeto == request.args(0, cast=int)).select()
    return locals()

@auth.requires_membership('operador')
def criar_class_desp():
    projeto = db.projeto(request.args(0, auth.user))
    
    db.class_desp.projeto.default = projeto.id
    db.class_desp.projeto.writable = False

    form = SQLFORM(db.class_desp).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_class_despesa', args=projeto.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_class_desp():
    class_desp = db.class_desp(request.args(0, cast=int))
    projeto = db.projeto(class_desp.projeto)
    db.class_desp.id.readable = False
    db.class_desp.id.writable = False
    
    db.class_desp.projeto.readable = False
    db.class_desp.projeto.writable = False

    form = SQLFORM(db.class_desp, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_class_despesa', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()


def acesso_despesa():
    class_desp = db.class_desp(request.args(0, cast=int))
    rows = db(db.despesa.class_desp == request.args(0, cast=int)).select(orderby=db.despesa.data_inicio)
    return locals()

@auth.requires_membership('operador')
def criar_desp():
    class_desp = db.class_desp(request.args(0, auth.user))
    
    db.despesa.class_desp.default = class_desp.id
    db.despesa.class_desp.writable = False

    form = SQLFORM(db.despesa).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_despesa', args=class_desp.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_desp():
    despesa = db.despesa(request.args(0, cast=int))
    class_desp = db.class_desp(despesa.class_desp)
    db.despesa.id.readable = False
    db.despesa.id.writable = False
    
    db.despesa.class_desp.readable = False
    db.despesa.class_desp.writable = False

    form = SQLFORM(db.despesa, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_despesa', args=class_desp.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
