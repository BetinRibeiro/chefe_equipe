# -*- coding: utf-8 -*-
# tente algo como
def index(): 
    listadias = [1,2,3]
    a = auth.user
    projeto = db.projeto(db.projeto.created_by == auth.user)
    rows_sub = db(db.sub_venda.projeto == projeto.id).select(orderby=~db.sub_venda.data_inicio)
    return locals()
