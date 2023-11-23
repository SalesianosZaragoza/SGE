# -*- coding: utf-8 -*-
# The first line is a special marker telling the Python interpreter that this 
# file has UTF-8, so that it can expect and handle non-ASCII characters.
from odoo import models, fields, api
class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True
    
    # On methods decorated with @api.multi the self represents a recordset. It can
    # contain a single record, when used from a form , or several records, when used
    # from a list view
    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
