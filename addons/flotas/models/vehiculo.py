# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class vehiculo(models.Model):
    _name = 'flotas.vehiculo'

    marca = fields.Char(string='marca', required=True, help='marca')
    color = fields.Selection(selection=[('1', 'Blanco'), ('2', 'Gris'), ('3', 'Negro')])
    numasientos = fields.Char(string='asientos', required=True, help='asientos')
    # Varios coche varios conductores
    conductores_ids = fields.Many2many('flotas.conductor', string="conductor")
    # Un coche varios viajes
    viajes_ids = fields.One2many('flotas.viaje','vehiculo_id', string="viajes")
    #fecharevision = 
    seguro_ids = fields.Many2one('flotas.seguro', string="viajes")