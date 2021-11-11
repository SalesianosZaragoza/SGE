# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Perros(models.Model):
    _name = "perritos"
    altura = fields.Integer(string="Altura del animal")
    raza = fields.Char(string="raza del animal")
    duenos_id = fields.Many2one("duenos", "dueños asociados")
    peso = fields.Integer(string="Peso del animal")
    imc = fields.Integer(string="calculo de indice mas corporal")
    age = fields.Float('Age', digits=(12, 1))
    _sql_constraints = [('raza', 'UNIQUE (raza)',
                         'ya existe un perro de esa raza')]

    @api.constrains('age')
    def _check_something(self):
        for record in self:
            if record.duenos_id.edad > 20:
                raise ValidationError("too old: %s" % record.age)

    def _compute_name(self):
        for record in self:
            record.raza = str(record.altura)

    @api.onchange('peso', 'altura')
    def _onchange_price(self):
        # set auto-changing field
        self.imc = self.peso * self.altura
        # Can optionally return a warning and domains
        if self.imc == 0:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "It was very bad indeed",
                }
            }


class Personas(models.Model):
    _name = "personas"
    dni = fields.Char(string="dni")


class Duenos(models.Model):
    _inherit = "personas"
    _name = "duenos"
    fecha_nac = fields.Date(string="Fecha Nacimiento", store=True)

    name = fields.Char(string="Nombre dueños", required=True)
    apellido = fields.Char(string="llido dueños", required=True)
    edad = fields.Float('Age', digits=(12, 1))
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
