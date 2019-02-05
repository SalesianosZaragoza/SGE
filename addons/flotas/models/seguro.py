# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class seguro(models.Model):
    _name = 'flotas.seguro'

    name = fields.Char(string='nombre', required=True, help='nombre de la compañia')
    fechadevencimiento = fields.Date(string='fecha de vencimiento', required=True)
    # (1)seguro (1)coche las normas son calras
    vehiculo_id = fields.One2many('flotas.vehiculo', inverse_name="seguro_ids", ondelete='set null', string="Vehicle", index=True)