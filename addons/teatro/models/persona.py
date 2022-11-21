# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class persona(models.Model):
    _name = 'teatro.persona'
    _description = 'Permite definir las características de una persona'
    _inherit = 'teatro.base'

    name = fields.Char(string='Nombre y apellidos')
    nacionalidad = fields.Char(string='Nacionalidad')