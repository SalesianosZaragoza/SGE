# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Provincia(models.Model):
    _name = 'touring.provincia'
    name = fields.Char(string="Nombre provincia", required=True)
    visita_id = fields.Many2one('touring.visit', string="Visita")
    poblacion_id = fields.One2many('touring.poblacion',
                                   'provincia_id',
                                   string="Poblacion")


class Poblacion(models.Model):
    _name = 'touring.poblacion'
    name = fields.Char(string="Nombre poblacion", required=True)
    visita_id = fields.Many2one('touring.visit', string="Visita")
    provincia_id = fields.Many2one('touring.provincia', string="Provincia")


class Turist(models.Model):
    _inherit = 'res.partner'
    visita_id = fields.One2many('touring.visit', 'tourist_id', string="Visita")


class Event(models.Model):
    _name = 'touring.event'
    name = fields.Char(string="Nombre del evento", required=True)
    description = fields.Char(string="Descripcion del evento")
    visit = fields.Many2many('touring.visit', 'event_visita', 'event_id',
                             'visit_id', 'Visit')


class Visit(models.Model):
    _name = 'touring.visit'

    start_date = fields.Date(string="Start Date",
                             store=True,
                             default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True)

    duration = fields.Float(digits=(6, 2),
                            help="Duration in days",
                            compute='_days_duration')

    tourist_id = fields.Many2one('res.partner', string="Turista")
    provincia_id = fields.Many2one('touring.provincia', string="Provincia")
    poblacion_id = fields.Many2one('touring.poblacion', string="Poblacion")
    event = fields.Many2many('touring.event', 'event_visita', 'visit_id',
                             'event_id', 'Event')
