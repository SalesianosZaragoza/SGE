from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'openacademy.curso'
    _description = "OpenAcademy Courses"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    description2 = fields.Text()
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions",
        domain="['seats' > 0]")
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    _sql_constraints = [
        ('loasdasdasddadas',
         'CHECK(name != description)',
         "The title of the course should not be the description")
    ]


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    course_id = fields.Many2one('openacademy.curso',
        ondelete='cascade', string="Course", required=True)
    unit_price = fields.Float(digits=(6, 2), help="price per unit")
    amount = fields.Float(digits=(6, 2), help="number of units")
    total = fields.Float(digits=(6, 2), help="total calculated price")
    total_with_iva = fields.Float(digits=(6, 2), help="total incl Iva", compute='_calculateIva')
    @api.depends('total')
    def _calculateIva(self):
        for r in self:
            if not r.total:
                r.total_with_iva = 0.0
            else:
                r.total_with_iva = r.total + ((r.total/100)*21)

    @api.onchange('amount', 'unit_price')
    def _onchange_price(self):
        # set auto-changing field
        self.total = self.amount * self.unit_price
        # Can optionally return a warning and domains
        if(self.amount<2):
            return {
                'warning': {
                    'title': "Low Amount",
                    'message': "Raise the amount",
                }
            }

    @api.constrains('duration')
    def _check_something(self):
        for record in self:
            if record.duration > 2:
                raise ValidationError("Excesive duration: %s" % record.duration)
    # all records passed the test, don't return anything