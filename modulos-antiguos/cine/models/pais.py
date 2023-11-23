# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pais(models.Model):
    _name = 'cine.pais'

    name = fields.Char()
    idsactores=fields.One2many('cine.actor','idpais',string="actor")