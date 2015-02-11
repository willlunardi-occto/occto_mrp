# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2015 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
#OCCTO - Comunicação criação e Tecnologia
#atendimento@occto.com.br  http://www.occto.com.br
#Fone: 94 3311-0407    Celular: 94 99280-2967
#Versão: 7.0.1 Revisão: 06/02/2015
##############################################################################


from openerp.osv import fields, osv, orm
from datetime import time, datetime
from tools.translate import _



class occtomrp_contrato(osv.osv):
    _name = 'occtomrp.contrato'
    _description = 'Formulario de Contratos'
    _columns = {
        'name':fields.char('Nome do Contrato', size=50, required=True,  help='Este campo e formado pelo nome do Cliente e Numero do Contrato'),
        'objeto_contrato':fields.char('Objeto do Contrato', size=400, help='Este campo e o objeto do contrato'),
        'data_inicio':fields.date('Data de Inicio', required=True),
        'data_fim':fields.date('Data de Fim', required=True),
        'state': fields.selection([('draft', 'Novo'), ('confirmed', 'Confirmado'), ('Cancel', 'Cancelado')], 'Estado', readonly=True),
        'active': fields.boolean('Ativo'),
        #Campos de relacionamento
        'empresa_cliente': fields.many2one('res.partner', 'Cliente', required=True)
        #id_sla
        #
    }
    _defaults = {
        #'name': lambda *a: datetime.now.strftime('%d-%m-%Y'),
        'state': 'draft',
        'active': 'True'
    }

occtomrp_contrato()



class mrp_production(osv.osv):
    _name = 'mrp.production'
    _inherit = 'mrp.production'
    _columns = {
        'contrato': fields.many2one('occtomrp.contrato', 'Contrato', required=True),
    }
    _defaults = {
    

    }

mrp_production()



