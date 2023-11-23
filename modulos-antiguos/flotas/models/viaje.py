# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class viaje(models.Model):
    _name = 'flotas.viaje'

    vehiculo_id = fields.Many2one('flotas.vehiculo', ondelete='set null', string="vehiculo", index=True)
    duracionhoras = fields.Date(string='tiempo de viaje', required=True)
    horas = fields.Char(string='horas', required=True, help='horas de viaje')
    # falta campo onchange!