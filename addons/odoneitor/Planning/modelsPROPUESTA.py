
from odoo import models, fields, api, exceptions

"""
Clase que representa un cliente
Campos:
    - String nombreEmpresa
Relaciones:
    - 1:N con Proyectos
"""
class Client(models.Model):
    _name = 'softonic.client'
    name  = fields.Char(string='Name', required=True, help='Name of the client...')
    # Un cliente contiene una lista de sus proyectos
    relatedProyects_ids = fields.one2Many(
        'softonic.proyect', 'client_id', string="Associated proyects"
    )
"""
Clase que representa un proyecto
Campos:
    - String Nombre
Relaciones:
    - 1:N con Proyectos
    - N:N con Lenguajes de Programación
    - N:N con Programadores -> generará tabla intermedia con el campo 'PUESTO'
"""
class Proyect(models.Model):
    _name = 'softonic.proyect'
    name  = fields.Char(string='Name', required=True, help='Name of the proyect...')
    # Un proyecto lleva una referencia a su cliente
    client_id = fields.Many2one('softonic.client',
        ondelete='set null', string="Client", index=True)
    # Un proyecto involucra varios lenguajes de programación
    langs_ids = fields.Many2many('softonic.language', string="Technologies used")
    # Relación con la tabla intermedia -> una lista de sus colaboraciones
    relatedTeams_ids = fields.one2Many(
        'softonic.team', 'proyect_id', string="Collaborations"
    )
"""
Clase que representa a un programador
Campos:
    - String Nombre
    - String Apellidos
    - Date fechaNacimiento
    - Date fechaIncorporacionEmpresa
Relaciones:
    - N:N con Lenguajes de Programación 
    - N:N con Proyectos
"""
class Coder(models.Model):
    _name    = 'softonic.coder'
    name     = fields.Char(string='Name', required=True, help='Name of the coder...')
    lastname = fields.Char(string='Last Name', required=True, help='Last Name of the proyect...')
    birthDate = fields.Date(string='Date of Birth', required=True)
    joinDate  = fields.Date(string='Hiring date', required=True)
    # Un programador conoce varios lenguajes de programación
    langs_ids = fields.Many2many('softonic.language', string="Known Programming Languages")
    # Relación con la tabla intermedia -> una lista de sus colaboraciones
    relatedTeams_ids = fields.one2Many(
        'softonic.team', 'coder_id', string="Collaborations"
    )
"""
Clase que representa un lenguaje de programación
Campos:
    - String Nombre
    - String Tipo
Relaciones:
    N:N con Programadores
    N:N con Proyectos
"""
class Language(models.Model):
    _name = 'softonic.language'
    name  = fields.Char(string='Name', required=True, help='Name of the language...')
    type  = fields.Char(string='Type', required=False, help='Additional info')
    # Un lenguaje de programación se usa en varios proyectos
    proyects_ids = fields.Many2many('softonic.proyect', string="Proyects")
    # Un lenguaje es conocido por varios programadores
    coders_ids = fields.Many2many('softonic.coder', string="Associated Pr0s")
"""
Tabla intermedia de la relación programadores / proyectos
Atributos propios:
    - String Puesto
    - Float HorasAsignadas
"""
class Team(models.Model):
    _name     = 'softonic.team'
    position  = fields.Char(string='Position', required=True, help='Programmer\'s position inside of the team...')
    hours     = fields.Float(digits=(6,2), required=False, help='Assigned hours...')
    # En el equipo debe haber una referencia al programador
    coder_id = fields.Many2one('softonic.coder',
        ondelete='set null', string="Coder", index=True)
    # En el equipo debe haber una referencia al proyecto
    proyect_id = fields.Many2one('softonic.proyect',
        ondelete='set null', string="Proyect", index=True)