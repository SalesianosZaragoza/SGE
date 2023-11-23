# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Client(models.Model):
    _name = 'softonic.client'
    name = fields.Char(string='Name', required=True,
                       help='Name of the client...')
    # Un cliente contiene una lista de sus proyectos
    relatedProyects_ids = fields.One2many(
        'softonic.proyect', 'client_id', string="Proyects")


class Coder(models.Model):
    _name = 'softonic.coder'
    name = fields.Char(string='Name', required=True,
                       help='Name of the coder...')
    lastname = fields.Char(string='Last Name', required=True,
                           help='Last Name of the coder...')
    birthDate = fields.Date(string='Date of Birth', required=True)
    joinDate = fields.Date(string='Hiring date', required=True)

    # Un programador conoce varios lenguajes de programación
    langs_ids = fields.Many2many(
        'softonic.language', string="Known Programming Languages")
    
    # Relación con la tabla intermedia -> una lista de sus colaboraciones
    relatedTeams_ids = fields.Many2many(
        'team.team', 'coder_id', string="Collaborations")


class Language(models.Model):
    _name = 'softonic.language'
    name = fields.Char(string='Name', required=True,
                       help='Name of the language...')

    # http://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html
    # !! CUIDADO !!
    # La documentación parece haberla escrito un **puto mono**, así que está mal!
    typeOfLanguage = type = fields.Selection(
        selection=[('oop', 'Orientado a objetos'), ('fp', 'Funcional')])

    # Un lenguaje de programación se usa en varios proyectos
    proyects_ids = fields.Many2many('softonic.proyect', string="Proyects")
    # Un lenguaje es conocido por varios programadores
    coders_ids = fields.Many2many('softonic.coder', string="Associated Pr0s")


class Proyect(models.Model):
    _name = 'softonic.proyect'
    name = fields.Char(string='Name', required=True,
                       help='Name of the proyect...')
    # Un proyecto lleva una referencia a su cliente
    client_id = fields.Many2one(
        'softonic.client', ondelete='set null', string="Clients", index=True)
    # Un proyecto involucra varios lenguajes de programación
    langs_ids = fields.Many2many(
        'softonic.language', string="Technologies used")

    # Relación con la tabla intermedia -> una lista de sus colaboraciones
    relatedTeams_ids = fields.One2many(
        'team.team', 'proyect_id', string="Collaborations")

    fecha_inicio = fields.Date(default=lambda self: fields.datetime.now())
    fecha_fin = fields.Date(string='Fecha fin', required=True)

class Team(models.Model):
    _inherit = 'team.team'
    # En el equipo debe haber una referencia al programador
    coders_ids = fields.Many2many('softonic.coder',
        ondelete='set null', string="Coder", index=True)
    # En el equipo debe haber una referencia al proyecto
    proyect_id = fields.Many2one('softonic.proyect',
        ondelete='set null', string="Proyect", index=True)
