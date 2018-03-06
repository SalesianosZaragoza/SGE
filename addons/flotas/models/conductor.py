# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class conductor(models.Model):
    _inherit = 'base.entidad'
    _name= 'flotas.conductor'

    name = fields.Char(string='nombre', required=True, help='nombre del conductor')
    dni = fields.Char(string='DNI', required=True, help='DNI del conductor')
    # En el conductor referencia a vehiculos
    vehiculos_ids = fields.Many2many('flotas.vehiculo', ondelete='set null', string="vehiculos", index=True)
