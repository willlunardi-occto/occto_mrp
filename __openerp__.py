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
#e-mail: atendimento@occto.com.br
#Fone: 94 3311-0407    Celular: 94 99280-2967
#Versão: 7.0.1 Revisão: 06/02/2015
##############################################################################


{
    'name' : 'Adaptação do Módulo MRP',
    'version' : '7.0.1',
    'category' : 'Manufatura',
    'description' : """
    Adaptação do módulo MRP para atender a necessidade no projeto de impalantação do OpeERP na CAEMCO.
    """,
    'author' : 'OCCTO',
    'website' : 'http://www.occto.com.br',
    'license' : 'AGPL-3',
    'depends' : ["mrp"],
    'init_xml' : [],
    'demo_xml' : [],
    'update_xml' : ['occtomrp_view.xml',],
    'active': False,
    'installable': True
}