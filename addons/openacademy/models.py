# -*- coding: utf-8 -*-

from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()