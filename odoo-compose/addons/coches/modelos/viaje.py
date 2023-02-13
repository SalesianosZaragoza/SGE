# -*- coding: utf-8 -*-

from odoo import models, fields, api

class viaje(models.Model):
    _name = 'examen.viaje'
    _description = 'viaje'

    vehiculo = fields.Many2one("examen.vehiculo", string="Vehiculo", required=True)
    provincia_origen = fields.Reference(selection=[('examen.provincia', 'Provincia')], string="Provincia de origen", required=True)
    provincia_destino = fields.Reference(selection=[('examen.provincia', 'Provincia')], string="Provincia de destino", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    duracion_horas = fields.Float(string="Duración (en horas)", required=True)
    es_largo = fields.Boolean(string="Es largo", compute="_compute_es_largo", store=True)

    @api.depends('duracion_horas')
    def _compute_es_largo(self):
        for record in self:
            record.es_largo = record.duracion_horas > 2