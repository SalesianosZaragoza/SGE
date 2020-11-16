from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.curso'
    _description = "OpenAcademy Courses"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    description2 = fields.Text()
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")



class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)