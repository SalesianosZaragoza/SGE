# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import persona

class actor(models.Model):
    _name = 'teatro.actor'
    _description = 'Permite definir las características de un actor'
    _inherit = 'teatro.persona'

    inicio_trayectoria = fields.Date(string='Fecha de inicio de trayectoria')
    personaje= fields.Char(string='Personaje interpretado')

    obra_ids = fields.Many2many('teatro.obra', string="Obras")