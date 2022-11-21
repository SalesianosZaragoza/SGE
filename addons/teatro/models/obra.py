# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class obra(models.Model):
    _name = 'teatro.obra'
    _description = 'Permite definir las características de una obra'
    _inherit = 'teatro.base'

    name = fields.Char(string='Título obra')
    genero = fields.Char(string='Género')
    idioma = fields.Char(string='Idioma')
    duracion = fields.Float(string='Duracion')
    estreno = fields.Date(string='Fecha de estreno')
    resumen = fields.Text(string='Resumen')

    sala_id = fields.Many2one('teatro.sala', string='Sala')
    director_id = fields.Many2one('teatro.director', string='Director')
    actor_ids = fields.Many2many('teatro.actor', string="Actores")
    promocion_ids = fields.Many2many('teatro.promocion', string="Promociones")
    opinion_ids = fields.One2many('teatro.opinion', 'obra_id', string="Opiniones")