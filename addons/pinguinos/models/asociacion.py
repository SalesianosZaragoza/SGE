from odoo import models, fields, api, exceptions

class Asociacion(models.Model):
    _name = 'simuexamen.asociacion'

    name = fields.Char(string="Nombre")
    pinguino_ids = fields.Many2one('simuexamen.pinguino', string="pinguinos")