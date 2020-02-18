# -*- coding: utf-8 -*-
db.define_table('projeto',
				#Informações da Venda
                Field('descricao', 'string', notnull=True, label="Descrição",requires = IS_UPPER()),
				Field('nome_chefe', 'string', label="Nome Chefe",requires = IS_UPPER()),
                Field('primeira_cidade', 'string', label="Primeira Cidade",requires = IS_UPPER()),
				Field('vale_chefe', 'double', label="Vale do Chefe",notnull=True, default=0),
                Field('descricao_vale', 'text', label="descricao vale do Chefe",requires = IS_UPPER()),
                Field('caderno_chefe', 'double', label="Caderno do Chefe",notnull=True, default=0),
				Field('descricao_caderno', 'text', label="descricao caderno do Chefe",requires = IS_UPPER()),
				Field('dinheiro_adiantado', 'double', label="Dinheiro Adiantado",notnull=True, default=0),
                Field('descricao_adiantamento', 'text', label="descricao adicnatamento",requires = IS_UPPER()),
                Field('comissao_chefe', 'double',  label="% Comissao Chefe",notnull=True, default=3),
                Field('data_saida', 'date', label="Data Saida", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                Field('data_cobranca', 'date', label="Data Cobrança", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),

                ##informação da despesa da venda
				Field('total_despesa', 'double', writable=False, readable=True, notnull=True, default=0),

				#informações Mercadoria e retorno
				Field('total_pecas_mercadoria', 'integer', writable=False, readable=True , notnull=True, default=0),
				Field('total_preco_mercadoria', 'double', writable=False, readable=True , notnull=True, default=0),

				Field('total_pecas_retorno', 'integer', writable=False, readable=False, notnull=True, default=0),
				Field('total_preco_retorno', 'double', writable=False, readable=False, notnull=True, default=0),

				#informações Funcionario
				Field('total_salario', 'double', writable=False, readable=True , notnull=False , default=0),
				Field('total_vale_saida_funcionario', 'double', writable=False, readable=True , notnull=True, default=0),
				Field('total_vale_caderno_funcionario', 'double', writable=False, readable=True , notnull=True, default=0),

                #informações vendedor
				Field('total_vale_saida_vendedor', 'double', writable=False, readable=True , notnull=True, default=0),
				Field('total_vale_caderno_vendedor', 'double', writable=False, readable=True , notnull=True, default=0),
				Field('total_venda_praso', 'double', writable=False, readable=True , notnull=True, default=0),
				Field('total_entradas_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('total_quant_fichas', 'integer', writable=False, readable=True , notnull=True, default=0),
				Field('total_comis_venda_vendedor', 'double', writable=False, readable=False, notnull=True, default=0),

                Field('total_venda_vista', 'double', writable=False, readable=True , notnull=True, default=0),
                auth.signature,
                format='%(descricao)s')

db.define_table('funcionario',
				Field('projeto','reference projeto', label='Equipe'),
				Field('nome_funcionario', 'string', label='Nome',requires = IS_UPPER()),
				Field('funcao', 'string', label='Função',requires = IS_UPPER()),
				Field('salario_funcionario', 'double', label='Salario',  notnull=True, default=1500),
				Field('vale_saida_funcionario', 'double', label='Vale da saida', notnull=True, default=0),
				Field('vale_caderno_funcionario', 'double', label='Vale do Caderno',  notnull=True, default=0),
                Field('descricao', 'text', label='Descrição do vale',requires = IS_UPPER()),
				auth.signature)

db.define_table('carrada',
                Field('projeto','reference projeto', label='Equipe'),
                Field('data_carrada', 'date', label="Data", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                Field('descricao', 'string', label='Descrição',requires = IS_UPPER()),                
                Field('cidade', 'string', label='Cidade',requires = IS_UPPER(), writable=False, readable=True , notnull=True, default="padão"),
                Field('total_pecas', 'integer', label='Quant. Peças', writable=False, readable=True , notnull=True, default=0),
				Field('total_preco', 'double', label='Total Preço', writable=False, readable=True , notnull=True, default=0),
                Field('total_custo', 'double', label='Total Custo', writable=False, readable=True , notnull=True, default=0),
				auth.signature,
                format='%(descricao)s')

db.define_table('mercadoria',
				Field('carrada','reference carrada', label='Carrada', writable=True, readable=True),
				Field('quant_pcs_enviada', 'integer', label='Quant Peças', notnull=True, default=0),
				Field('descricao', 'string',label='Descrição', notnull=True,requires = IS_UPPER()),
				Field('preco_unitario', 'double',label='Preço Unit', notnull=True, default=0),
				Field('quant_pcs_retorno', 'integer',label='Quant Peças Retorno', writable=False, readable=False, default=0, notnull=True),
				auth.signature)

db.define_table('vendedor',
				Field('projeto','reference projeto', label='Equipe', writable=True, readable=True),
				Field('nome_vendedor', 'string', label='Nome',requires = IS_UPPER()),
				Field('vale_saida', 'double',label='Vale da Saida', notnull=True, default=0),
				Field('vale_caderno', 'double',label='Vale Caderno', writable=False, readable=True , notnull=True, default=0),
				Field('vendapraso', 'double', label='Venda a Praso',writable=False, readable=True , notnull=True, default=0),
                Field('vendavista', 'double', label='Venda à Vista',writable=False, readable=True , notnull=True, default=0),
				Field('entradas_venda', 'double', label='Entrada Venda',writable=False, readable=True , notnull=True, default=0),
				Field('quant_fichas', 'integer', label='Quant Fichas',writable=False, readable=True , notnull=True, default=0),
				Field('comissao_venda', 'double',label='% Comissão', notnull=True, default=7),
                Field('descricao', 'text', label='Descrição do vale',requires = IS_UPPER()),
				auth.signature,
                format='%(nome_vendedor)s')

db.define_table('sub_venda',
				Field('projeto','reference projeto', label='Projeto', writable=True, readable=True),
                Field('data_inicio', 'date', label="Data Inicio", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                Field('data_cob', 'date', label="Data Cobrança", writable=False, readable=False, default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                Field('descricao', 'string', label='Descrição',requires = IS_UPPER()),
				Field('quant_fichas', 'integer', label='Quant Fichas', writable=False, readable=False, notnull=True, default=0),
				Field('venda_praso', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('entradas_venda', 'double', writable=False, readable=False, notnull=True, default=0),
				Field('venda_vista', 'double', writable=False, readable=False, notnull=True, default=0),
				auth.signature,
                format='%(descricao)s')

db.define_table('venda',
				Field('sub_venda','reference sub_venda', label='Sub-Venda', writable=True, readable=True),
                Field('vendedor','reference vendedor', label='Vendedor', writable=True, readable=True),
                Field('data_venda', 'date', label="Data", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
				Field('vale_caderno', 'double', label='Vale Caderno', notnull=True, default=0),
				Field('quant_fichas', 'integer', label='Quant Fichas', notnull=True, default=0),
				Field('venda_praso', 'double', label='Venda Praso', notnull=True, default=0),
				Field('entradas_venda', 'double', label='Entrada', notnull=True, default=0),
				Field('venda_vista', 'double', writable=False, readable=False, label='Venda à Vista', notnull=True, default=0),
                Field('quant_fichas_devolvidas', 'integer', label='Quant Fichas Devolvidas', notnull=True, default=0),
                Field('valor_devolvido', 'double', label='Valor Devolvido', notnull=True, default=0),
                Field('descricao_devolucao', label='Descrição do Caderno',requires = IS_UPPER()),

				auth.signature)

db.define_table('class_desp',
                Field('projeto','reference projeto', label='Equipe'),
                Field('descricao', 'string', label='Descrição',requires = IS_UPPER()),
				Field('total_classe', 'double', label='Total', writable=False, readable=True , notnull=True, default=0),
				auth.signature,
                format='%(descricao)s')

db.define_table('despesa',
				Field('class_desp','reference class_desp', label='Classe', writable=True, readable=True),
                Field('data_inicio', 'date', label="Data Inicio", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
				Field('descricao', 'string',label='Descrição', default="DESPESA", notnull=True,requires = IS_UPPER()),
				Field('valor', 'double',label='Valor', notnull=True, default=0),
				auth.signature)

db.define_table('avista',
				Field('projeto','reference projeto', label='Projeto', writable=False, readable=False),
                Field('data_venda', 'date', label="Data", default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
				Field('cidade', 'string',label='Cidade', notnull=True,requires = IS_UPPER()),
				Field('valor', 'double',label='Valor', notnull=True, default=0),
				auth.signature)
