from odoo import models, fields, api, exceptions

class Padrino(models.Model):
    _name = 'simuexamen.padrino'

    name = fields.Char(string="Nombre")
    fecha = fields.Datetime(string="fecha")
    pinguino_ids = fields.Many2one('simuexamen.pinguino', string="Pinguinos")