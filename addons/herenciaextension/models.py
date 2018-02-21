# -*- coding: utf-8 -*-

from odoo import models,fields


    
class alumno(models.Model):
    _inherit = 'base.entidad'
    fechaCumple = fields.Date()

