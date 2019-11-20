import random
# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Heredar(models.Model):
    #se almacena en una tabla nueva que se llamara
    #openacademy heredar
    _name ='openacademy.heredar'
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

    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    name = fields.Char(required=True)
    seats = fields.Integer(string="Number of seats")
    aleatorio = fields.Char(required=True)
    email = fields.Char(required=True, compute='_random')
    precio = fields.Integer()
    num_unidades = fields.Integer()
    total = fields.Integer(compute='total')
    confirmed = fields.selection((('n','Unconfirmed'), 
                    ('c','Confirmed'))


    @api.multi
    def _random(self):
        for record in self:
            record.aleatorio = str(random.randint(1, 1e6))

    @api.depends('precio','num_unidades')
    def total(self):
        for record in self:
            record.total = record.precio * record.num_unidades


    # onchange handler
    @api.onchange('email')
    def cambio_de_precio(self):
        # set auto-changing field
        print(self.email)
        if self.email.str.find("@") == -1:
        # Can optionally return a warning and domains
            return {
               'warning': {
                    'title': "email not valid",
                    'message': "email no valido"
                }
            }