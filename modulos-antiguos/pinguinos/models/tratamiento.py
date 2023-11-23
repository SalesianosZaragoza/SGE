from odoo import models, fields, api, exceptions

class Tratamiento(models.Model):
    _name = 'simuexamen.tratamiento'

    name = fields.Char(string="Nombre")
    fecha = fields.Datetime(string="fecha")
    duracion = fields.Integer(string="en horas")
    ingreso = fields.Boolean(string="necesita el pinguino ingreso?")
    pinguino_id = fields.Many2one('simuexamen.pinguino', string="pinguino", ondelete='cascade')

    @api.onchange('duracion')
    def do_stuff(self):
        if self.duracion >= 24:
            self.ingreso = 'True'
            

                