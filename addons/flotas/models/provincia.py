# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime

class provincia(models.Model):
    _name = 'flotas.provincia'

    name = fields.Char(string='nombre', required=True, help='nombre de la provincia')