# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pelicula(models.Model):
    _name = 'cine.pelicula'

    name = fields.Char()
    description = fields.Text()
    idirector = fields.Many2one('cine.director',String="director")
    idsactores=fields.Many2many(string= "actores",comodel_name='cine.actor',relation = 'rel_actores_peliculas',column1='pelicula', column2='actor')