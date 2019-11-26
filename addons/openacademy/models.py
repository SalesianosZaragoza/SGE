# -*- coding: utf-8 -*-
import random
from datetime import timedelta
from odoo import fields, models, api

class Heredar(models.Model):
    #se almacena en una tabla nueva que se llamara
    #openacademy heredar
    _name = 'openacademy.heredar'
    _inherit = 'base.empresa'
    codigoPostal = fields.Char(string="codigo postal")

class Extender(models.Model):
    #NO se crea una tabla nueva en la base de datos
    _inherit = 'base.empresa'
    dni = fields.Char(string="dni")

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()

class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    duration = fields.Float(digits=(6, 2), help="Duration in days")
    name = fields.Char(required=True)
    seats = fields.Integer(string="Number of seats")
    aleatorio = fields.Char()
    email = fields.Char(compute='_random')
    precio = fields.Integer()
    num_unidades = fields.Integer()
    total = fields.Integer(compute='_total')
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    confirmed = fields.Selection([('n', 'Unconfirmed'), ('c', 'Confirmed')])
    start_date = fields.Date(default=fields.Date.today) 
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            r.duration = (r.end_date - r.start_date).days + 1


    @api.multi
    def _random(self):
        for record in self:
            record.email = str(random.randint(1, 1e6))

    @api.depends('precio', 'num_unidades')
    def _total(self):
        for record in self:
            record.total = record.precio * record.num_unidades


    # onchange handler
    @api.onchange('precio','num_unidades')
    def cambio_de_precio(self):
        # set auto-changing field
        if self.precio < 0 or self.num_unidades < 0:
        # Can optionally return a warning and domains
            return {
                'warning': {
                    'title': "price not valid",
                    'message': "precio no valido"
                }
            }
        else :
            self.total = self.precio * self.num_unidades
