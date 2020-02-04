# -*- coding: utf-8 -*-
def acesso_equipe():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.vendedor.projeto == request.args(0, cast=int)).select(orderby=~db.vendedor.vendapraso)
    return locals()
@auth.requires_membership('operador')
def criar_vendedor():
    projeto = db.projeto(request.args(0, auth.user))
    
    db.vendedor.projeto.default = projeto.id
    db.vendedor.projeto.writable = False

    form = SQLFORM(db.vendedor).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_equipe', args=projeto.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_vendedor():
    vendedor = db.vendedor(request.args(0, cast=int))
    projeto = db.projeto(vendedor.projeto)
    db.vendedor.id.readable = False
    db.vendedor.id.writable = False
    
    db.vendedor.projeto.readable = False
    db.vendedor.projeto.writable = False

    form = SQLFORM(db.vendedor, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_equipe', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def acesso_particao():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.sub_venda.projeto == request.args(0, cast=int)).select()
    return locals()

@auth.requires_membership('operador')
def criar_particao():
    projeto = db.projeto(request.args(0, auth.user))
    
    db.sub_venda.projeto.default = projeto.id
    db.sub_venda.projeto.writable = False

    form = SQLFORM(db.sub_venda).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_equipe', args=projeto.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_particao():
    sub_venda = db.sub_venda(request.args(0, cast=int))
    projeto = db.projeto(sub_venda.projeto)
    db.sub_venda.id.readable = False
    db.sub_venda.id.writable = False
    
    db.sub_venda.projeto.readable = False
    db.sub_venda.projeto.writable = False

    form = SQLFORM(db.sub_venda, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_equipe', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def acesso_venda():
    vendedor = db.vendedor(request.args(0, cast=int))
    rows_sub = db(db.sub_venda.projeto == vendedor.projeto).select(orderby=~db.sub_venda.data_inicio)
    rows_vend = db(db.venda.vendedor == request.args(0, cast=int)).select(orderby=db.venda.data_venda)
    return locals()
@auth.requires_membership('operador')
def inserir_venda():
    vendedor = db.vendedor(request.args(0, auth.user))
    sub_venda = db.sub_venda(request.args(1, auth.user))
    
    db.venda.sub_venda.default = sub_venda.id
    db.venda.sub_venda.writable = False
    db.venda.sub_venda.readable = False
    
    db.venda.vendedor.default = vendedor.id
    db.venda.vendedor.writable = False

    form = SQLFORM(db.venda).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_venda', args=vendedor.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_venda():
    venda = db.venda(request.args(0, cast=int))
    vendedor = db.vendedor(venda.vendedor)
    db.venda.id.readable = False
    db.venda.id.writable = False
        
    db.venda.sub_venda.default = venda.sub_venda
    db.venda.sub_venda.writable = False
    db.venda.sub_venda.readable = False

    db.venda.vendedor.readable = False
    db.venda.vendedor.writable = False

    form = SQLFORM(db.venda, request.args(0, cast=int), deletable=True)
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_venda', args=vendedor.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()

def acesso_funcionario():
    projeto = db.projeto(request.args(0, cast=int))
    rows = db(db.funcionario.projeto == request.args(0, cast=int)).select(orderby=~db.funcionario.vale_saida_funcionario)
    return locals()
@auth.requires_membership('operador')
def criar_funcionario():
    projeto = db.projeto(request.args(0, auth.user))
    
    db.funcionario.projeto.default = projeto.id
    db.funcionario.projeto.writable = False

    form = SQLFORM(db.funcionario).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_funcionario', args=projeto.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return locals()
@auth.requires_membership('operador')
def alterar_funcionario():
    funcionario = db.funcionario(request.args(0, cast=int))
    projeto = db.projeto(funcionario.projeto)
    db.funcionario.id.readable = False
    db.funcionario.id.writable = False
    
    db.funcionario.projeto.readable = False
    db.funcionario.projeto.writable = False

    form = SQLFORM(db.funcionario, request.args(0, cast=int))
    if form.process().accepted:
        session.flash = 'Atualizado'
        redirect(URL('acesso_funcionario', args=projeto.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return locals()
