# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime
from dateutil.relativedelta import relativedelta

class director(models.Model):
    _name = 'cine.director'
    idsPeliculas=fields.One2many('cine.pelicula','idirector',String="pelicula")

    fechaActual=date.today()

    name = fields.Char()
    Fecha_Nacimiento = fields.Date()
    Edad = fields.Integer(compute="_value_pc", store=True)

    description = fields.Text()

    @api.onchange('Fecha_Nacimiento')
    def _value_pc(self):
        for r in self:
            if r.Fecha_Nacimiento:
                dt=r.Fecha_Nacimiento
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                self.Edad=relativedelta(self.fechaActual,d1).years
                return {
                    'warning': {
                    'title': "Edad",
                    'message': "La Edad Ha sido actualizada",
                    },
                }