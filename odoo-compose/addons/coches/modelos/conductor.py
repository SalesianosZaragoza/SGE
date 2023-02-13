# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conductor(models.Model):
    _name = 'examen.conductor'
    _description = 'conductor'

    nombre = fields.Char(string="Nombre", required=True)
    dni = fields.Char(String="DNI", required=True)
    vehiculo = fields.One2many("examen.vehiculo", "conductor", string="Vehiculo")