# -*- coding: utf-8 -*-

from odoo import models, fields, api

class provincia(models.Model):
    _name = 'examen.provincia'
    _description = 'provincia'
    
    nombre = fields.Char(string="Nombre", required=True)