# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class sala(models.Model):
    _name = 'teatro.sala'
    _description = 'Permite definir las características de una sala'
    _inherit = 'teatro.base'

    name = fields.Char(string='Nombre sala')
    num_butacas = fields.Integer(string='Cantidad butacas')
    
    obra_ids = fields.One2many('teatro.obra', 'sala_id', string="Obras")