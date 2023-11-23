# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Provincia(models.Model):
    _name = 'soci.provincia'
    name = fields.Char(string="Nombre provincia", required=True)
    poblacion_id = fields.One2many(
        'soci.poblacion', 'provincia_id', string="Poblacion")


class Poblacion(models.Model):
    _name = 'soci.poblacion'
    name = fields.Char(string="Nombre poblacion", required=True)
    provincia_id = fields.Many2one('soci.provincia', string="Provincia")
    cliente_id = fields.One2many(
        'soci.cliente', 'poblacion_id', string="Cliente")


class Clientes(models.Model):
    _name = 'soci.cliente'
    name = fields.Char(string="Nombre cliente", required=True)
    empleado_id = fields.Many2one('soci.empleado', string="Empleado")
    poblacion_id = fields.Many2one('soci.poblacion', string="Poblacion")
    weed_id = fields.Many2many(
        'soci.weed', 'cliente_weed', 'cliente_id', 'weed_id', 'Weed')
    gramos = fields.Float(digits=(2, 2), string="gramos",
                          help="Total de gramos")
    fechaIncorporacion = fields.Date(
        string="Fecha incorporacion", store=True, default=fields.Date.today)


class Empleados(models.Model):
    _name = 'soci.empleado'
    name = fields.Char(string="Nombre empleado", required=True)
    cliente_id = fields.One2many(
        'soci.cliente', 'empleado_id', string="Cliente")
    event_id = fields.One2many('soci.event', 'empleado_id', string="Evento")
    _inherit = 'base.entidad'


class Weed(models.Model):
    _name = 'soci.weed'
    name = fields.Char(string="Nombre Weed", required=True)
    indica = fields.Boolean(string="Indica")
    sativa = fields.Boolean(string="Sativa")
    gramos = fields.Float(digits=(3, 2), string="gramos",
                          help="Total de gramos", compute='_calcularG')
    cliente_id = fields.Many2many(
        'soci.cliente', 'cliente_weed', 'weed_id', 'cliente_id', 'Clientes')

    @api.one
    def _calcularG(self):
        gramosT = 0
        for cliente in self.cliente_id:
            gramosT += cliente.gramos
            self.gramos = gramosT


class Event(models.Model):
    _name = 'soci.event'
    name = fields.Char(string="Nombre del evento", required=True)
    description = fields.Char(string="Descripcion del evento")
    empleado_id = fields.Many2one('soci.empleado', string="Empleado")
    start_date = fields.Date(
        string="Start Date", store=True, default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True)

    duration = fields.Float(
        digits=(6, 2), help="Duration in days", compute='_days_duration')

    @api.one
    def _days_duration(self):
        if (self.end_date and self.start_date):
            start = fields.Datetime.from_string(self.start_date)
            end = fields.Datetime.from_string(self.end_date)
            self.duration = (end - start).days + 1

    @api.onchange('start_date', 'end_date')
    def _days_changed(self):
        for days in self:
            if(days.start_date or days.end_date):
                start = fields.Datetime.from_string(self.start_date)
                end = fields.Datetime.from_string(self.end_date)
                self.duration = (end - start).days + 1
                return {
                    'warning': {
                        'title': "Duration",
                        'message': "La duracion ha sido actualizada",
                    },
                }
