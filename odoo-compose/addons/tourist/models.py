# -*- coding: utf-8 -*-

import random
from odoo import models, fields, api


class Perros(models.Model):
    _name = "perritos"
    altura = fields.Integer(string="Altura del animal")
    raza = fields.Char(string="raza del animal", compute="_compute_name")
    duenos_id = fields.Many2one("duenos", "dueños asociados")
    peso = fields.Integer(string="Peso del animal")
    imc = fields.Integer(string="calculo de indice mas corporal")
    age = fields.Float('Age', digits=(12, 1))

    @api.constrains('age')
    def _check_something(self):
        for record in self:
            if record.age > 20:
                raise ValidationError("too old: %s" % record.age)

    @api.depends('altura')
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
    name = fields.Char(string="Nombre dueños", required=True)
    apellido = fields.Char(string="llido dueños", required=True)
    perros_id = fields.One2many('perritos',
                                'duenos_id',
                                string="Perros asociados")


class Vets(models.Model):
    _inherit = "personas"
    especialidad = fields.Selection([
        ('al', 'Alimen os'),
        ('ci', 'Cirugia'),
    ], 'ci')



