# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Perros(models.Model):
    _name = "perritos"
    altura = fields.Integer(string="Altura del animal")
    raza = fields.Char(string="raza del animal", compute="_compute_name")
    duenos_id = fields.Many2one("duenos", "dueños asociados")

    @api.depends('altura')
    def _compute_name(self):
        for record in self:
            record.raza = "hola" % str(record.altura)


class Personas(models.Model):
    _name = "personas"
    dni = fields.Char(string="dni")


class Duenos(models.Model):
    _inherit = "personas"
    _name = "duenos"
    name = fields.Char(string="Nombre dueños", required=True)
    apellido = fields.Char(string="Apellido dueños", required=True)
    perros_id = fields.One2many('perritos',
                                'duenos_id',
                                string="Perros asociados")


class Vets(models.Model):
    _inherit = "personas"
    especialidad = fields.Selection([
        ('al', 'Alimen os'),
        ('ci', 'Cirugia'),
    ], 'ci')


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