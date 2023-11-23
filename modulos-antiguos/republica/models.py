# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Jedi(models.Model):
    _name = 'republica.jedi'
    _inherit = 'base.entidad'
    sableLuz = fields.Selection(selection=[('1', 'Azul'), ('2', 'Verde'), (
        '3', 'Morado')], string="color del sable luz", default="1", compute="_color_morado")
    sith_id = fields.One2many('republica.sith', 'jedi_id', string="sith")
    fechaVisto = fields.Date(
        string="Fecha ultima vez visto", store=True, default=fields.Date.today)
    planeta_id = fields.Many2one('republica.planeta', string="planeta")
    midiclorianos = fields.Integer(string="midiclorianos")
    nivel = fields.Char(string="nivel", compute="_calcular_nivel")
    @api.one
    def _calcular_nivel(self):
        resultado = 0
        for r in self:
            resultado += r.midiclorianos
            if resultado < 100:
                self.nivel = "padawan"
            if resultado > 100 and resultado < 1000:
                self.nivel = "caballero"
            if resultado > 1000:
                self.nivel = "maestro"

    @api.one
    def _color_morado(self):
        if self.nivel == "padawan":
            self.sableLuz = '1'
        if self.nivel == "caballero":
            self.sableLuz = '2'
        if self.nivel == "maestro":
            self.sableLuz = '3'


class Sith(models.Model):
    _name = 'republica.sith'
    _inherit = 'base.entidad'
    raza_id = fields.Many2one('republica.especie', string="Raza")
    rabia = fields.Integer(string="rabia")
    oscuridad = fields.Integer(string="oscuridad")
    sableLuz = fields.Selection(selection=[(
        '1', 'Rojo'), ('2', 'Rojo Oscuro')], string="color del sable luz", default="1")
    usa2Sables = fields.Boolean(string="usa 2 sables")
    jedi_id = fields.Many2one('republica.jedi', string="jedi")
    @api.onchange('rabia')
    def _calcular_oscuridad(self):
        oscuridad = 0
        for r in self:
            oscuridad = r.rabia + r.rabia
            self.oscuridad = oscuridad


class Planetas(models.Model):
    _name = 'republica.planeta'
    name = fields.Char(string="Nombre planeta", required=True)
    jedi_id = fields.One2many('republica.jedi', 'planeta_id', string="jedi")
    destruido = fields.Boolean(string="Destruido por la estrella de la muerte")
    fechaDestruido = fields.Date(
        string="Fecha planeta destruido por la estrella de la muerte", store=True, default=fields.Date.today)
    raza_id = fields.One2many(
        'republica.especie', 'planeta_id', string="especie", compute="_quitar_raza")
    start_date = fields.Date(
        string="Start Date", store=True, default=fields.Date.today)

    @api.one
    def _quitar_raza(self):
        if self.destruido == True:
            self.raza_id = None


class Especie(models.Model):
    _name = 'republica.especie'
    name = fields.Char(string="Raza", required=True)
    planeta_id = fields.Many2one('republica.planeta', string="Planeta")
