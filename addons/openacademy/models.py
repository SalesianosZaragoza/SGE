# -*- coding: utf-8 -*-
from odoo import fields, models


class Heredar(models.Model):
    #se almacena en una tabla nueva que se llamara
    #openacademy heredar
    _name='openacademy.heredar'
    codigoPostal=fields.Char(string="codigo postal")

class Extender(models.Model):
    #NO se crea una tabla nueva en la base de datos
    _inherit='base.empresa'
    dni=fields.Char(string="dni")


class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    
class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    
    