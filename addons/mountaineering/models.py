# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime
from dateutil.relativedelta import relativedelta

class montana(models.Model):
    _name = 'mountaineering.montana'
    nombre = fields.Char()
    dificultad = fields.Selection([('dif1','Facil'),('dif2','Medio'),('dif3','Dificil')],'dif',default='dif1')
    idescalador =fields.One2many('mountaineering.escalador','idescalador',string="escalador")
    idascenso = fields.One2many('mountaineering.ascenso','idascenso',string="ascenso")
    idcompania = fields.Many2one('base.empresa',string="empresa")
    idmontana = fields.Many2one('mountaineering.montana',string="montana")
   
class escalador(models.Model):
    _inherit = 'base.entidad'
    _name = 'mountaineering.escalador'
    dni = fields.Char()
    idmontana =fields.One2many('mountaineering.montana','idmontana',string="montana")
    idescalador = fields.Many2one('mountaineering.escalador',string="escalador")

class compania(models.Model):
    _inherit = 'base.empresa'
    sherpas = fields.Char()
   
class ascenso(models.Model):
    _name = 'mountaineering.ascenso'
    idmontana = fields.Many2one('mountaineering.montana',string="montana")
    provincia = fields.Many2one('mountaineering.provincia',string="provincia")
    fecha  = fields.Date()
    metros = fields.Float()
    mayorochomilmetros = fields.Boolean(compute='_mayorochomilmetros')
    idascenso = fields.Many2one('mountaineering.ascenso',string="ascenso")

    @api.onchange('metros')
    def _mayorochomilmetros(self):
        for r in self:
            if r.metros > 8000:
                r.mayorochomilmetros = True
            else:
                r.mayorochomilmetros = False
   
class provincia(models.Model):
    _name = 'mountaineering.provincia'
    nombre = fields.Char()
    