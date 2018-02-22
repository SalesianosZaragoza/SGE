# -*- coding: utf-8 -*-

from odoo import models,fields
 
class alumno(models.Model):
    _inherit = 'base.entidad'
    fechaCumple = fields.Date()
    colegios = fields.Many2one('herenciaextension.colegio', string="Colegios")

class colegio(models.Model):
    _name = 'herenciaextension.colegio'
    nombre = fields.Char()
    fechaCumple = fields.Date()
    alumnos = fields.One2many('base.entidad','colegios', string="Alumnos")
