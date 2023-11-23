# -*- coding: utf-8 -*-

from odoo import models,fields


    
class empresa(models.Model):
    _name = 'base.empresa'
    nombreEmpresa = fields.Char(string="nombre empresa")

class entidad(models.Model):
    _name = 'base.entidad'
    nombreEntidad = fields.Char(string="nombre persona")

