# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import persona

class actor(models.Model):
    _name = 'teatro.director'
    _description = 'Permite definir las características de una director'
    _inherit = 'teatro.persona'

    destreza = fields.Char(string='Destreza')
    experiencia = fields.Text(string='Experiencia')

    obra_ids = fields.One2many('teatro.obra', 'director_id', string="Obras")