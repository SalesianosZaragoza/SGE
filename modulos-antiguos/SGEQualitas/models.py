# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta,date,datetime
from dateutil.relativedelta import relativedelta

    
class empresa(models.Model):
    _inherit = 'res.partner'
    direccion = fields.Char()
    codigo_postal = fields.Integer()
    alumnos_ids = fields.One2many('qualitas.alumno', 'empresa_id', string="Alumnos", domain=[('can_do_fct','=',True)])


class colegio(models.Model):
    _inherit = 'res.partner'
    _name = 'qualitas.colegio'

    name = fields.Char()
    alumnos_ids = fields.One2many('qualitas.alumno', 'colegio_id', string="Alumnos")
    n_alumnos = fields.Integer(compute='_calc_nalumnos')
    
    @api.depends('n_alumnos', 'alumnos_ids')
    def _calc_nalumnos(self):
        for r in self:
            r.n_alumnos = len(r.alumnos_ids)
    
   
class alumno(models.Model):
    _inherit = 'res.partner'
    _name = 'qualitas.alumno'
    
    name = fields.Char()
    fecha_nacimiento = fields.Date()
    can_do_fct = fields.Boolean(compute='_can_do_fct')
    edad = fields.Integer()
    examenes_suspendidos = fields.Integer(store=True, compute='_calc_exam_sus')
    colegio_id = fields.Many2one('qualitas.colegio', string="Colegio", ondelete = 'cascade')
    empresa_id = fields.Many2one('res.partner', string="Empresa", ondelete = 'cascade')
    examenes_ids = fields.Many2many(string= "Examenes" , comodel_name = 'qualitas.examen', relation = 'rel_examen_alumno', column1='alumno', column2='examen')
    ausencias_ids = fields.One2many('qualitas.ausencia', 'alumno_id', string="Ausencias")
    
    @api.depends('examenes_ids', 'examenes_suspendidos')
    def _calc_exam_sus(self):
        r.examenes_suspendidos = 0
        for r in self:
            r.examenes_suspendidos = len(r.examenes_ids)
    
    @api.depends('can_do_fct', 'examenes_suspendidos')
    def _can_do_fct(self):
        for r in self:
            if r.examenes_suspendidos < 2:
                r.can_do_fct = True
            else:
                r.can_do_fct = False
                
    @api.onchange('fecha_nacimiento')
    def set_age(self):
        for r in self:
            if r.fecha_nacimiento:
                dt = r.fecha_nacimiento
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                d2 = date.today()
                rd = relativedelta(d2, d1)
                r.age = rd.years  
                return {
                    'warning': {
                    'title': "Edad",
                    'message': "La Edad Ha sido actualizada",
                    },
                }
                
     
class examen(models.Model):
    _name = 'qualitas.examen'

    name = fields.Char()
    fecha_realizacion = fields.Date()
    hora = fields.Integer()
    asignatura = fields.Char()
    nota = fields.Integer()
    examenes_ids = fields.Many2many(string= "Alumnos" , comodel_name = 'qualitas.alumno', relation = 'rel_examen_alumno', column1='examen', column2='alumno')
    asignatura = fields.Selection([('asig1','Entornos'), ('asig2','Sist Gest')], 'Asig', default='asig1')
    
class ausencia(models.Model):
    _name = 'qualitas.ausencia'

    name = fields.Char()
    fecha = fields.Date()
    horas = fields.Integer()
    alumno_id = fields.Many2one('qualitas.alumno', string="Alumno", ondelete = 'cascade')
    
