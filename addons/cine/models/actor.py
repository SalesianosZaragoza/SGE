# -*- coding: utf-8 -*-

from odoo import models, fields, api

class actor(models.Model):
    _name = 'cine.actor'

    name = fields.Char()
    edad = fields.Integer()
    idpais=fields.Many2one('cine.pais',string="pais")
    idspeliculas=fields.Many2many(string= "peliculas",comodel_name='cine.pelicula',relation = 'rel_actores_peliculas',column1='actor', column2='pelicula')
