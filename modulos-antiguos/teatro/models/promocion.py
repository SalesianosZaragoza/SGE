# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class promocion(models.Model):
    _name = 'teatro.promocion'
    _description = 'Permite definir las características de una promo'
    _inherit = 'teatro.base'

    descuento = fields.Integer(string='Descuento')

    obra_ids = fields.Many2many('teatro.obra', string="Obras")