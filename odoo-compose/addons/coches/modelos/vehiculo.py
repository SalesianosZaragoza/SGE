# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'examen.vehiculo'
    _description = 'vehiculo'

    marca = fields.Char(string="Marca", required=True)
    color = fields.Char(string="Color", required=True)
    cantidad_de_asientos = fields.Integer(String="Cantidad de asientos", required=True)
    conductor = fields.Many2one("examen.conductor", string="Conductor")
    viajes = fields.One2many("examen.viaje", "vehiculo", string="Viajes")
    seguro = fields.Reference(selection=[('examen.seguro', 'Seguro')], string="Seguro", required=True)