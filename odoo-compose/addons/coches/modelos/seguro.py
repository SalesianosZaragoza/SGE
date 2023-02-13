# -*- coding: utf-8 -*-

from odoo import models, fields, api

class seguro(models.Model):
    _name = 'examen.seguro'
    _description = 'seguro'
    
    compania = fields.Char(string="Compañia", required=True)
    fecha_de_vencimiento = fields.Date(string="Fecha de vencimiento", required=True)   
    vehiculo = fields.Reference(selection=[('examen.vehiculo', 'Vehiculo')], string="Vehiculo")
