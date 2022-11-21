# -*- coding: utf-8 -*-

from odoo import models, fields, api

class opinion(models.Model):
    _name = 'teatro.opinion'
    _description = 'Permite definir las características de una opinion'

    nombre = fields.Char(string='Nombre del crítico')
    edad = fields.Integer(string='Edad del crítico')
    fecha = fields.Date(string='Fecha de la crítica')
    nota = fields.Integer(string='Nota')
    comentarios = fields.Text(string='Comentarios')

    obra_id = fields.Many2one('teatro.obra', string='Obra')

