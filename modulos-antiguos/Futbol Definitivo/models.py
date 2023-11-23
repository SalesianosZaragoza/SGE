from datetime import timedelta
from odoo import models, fields, api, exceptions


class Equipo(models.Model):
    _name = 'equipo.modelo'
    _description = "Modulo Equipo"

    name = fields.Char(string="Equipo", required=True)
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Entrenador", index=True)
    jugadores_ids = fields.One2many('jugador.modelo', 'equipo_id', string="Jugadores")
    description = fields.Text(string="Descripcion")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copia de {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copia de {}".format(self.name)
        else:
            new_name = u"Copia de {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Equipo, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "El nombre del equipo no puede ser el mismo que la descripcion"),

        ('name_unique',
         'UNIQUE(name)',
         "Ya existe un equipo con este nombre!"),
    ]

class Jugador(models.Model):
    _name = 'jugador.modelo'
    _description = "Modulo Jugador"

    name = fields.Char(required=True, string="Jugador")
    start_date = fields.Date(string="Fecha del fichaje", default=fields.Date.today)
    end_date = fields.Date(string="Fecha de despedida", store=True, compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(digits=(6, 2), help="Duration in days", string="Tiempo en el equipo")
    goals = fields.Integer(string="Numero de goles")
    active = fields.Boolean(default=True, string="Actualmente en el equipo")

    # instructor_id = fields.Many2one('res.partner', string="Entrenador")
    equipo_id = fields.Many2one('equipo.modelo', ondelete='cascade', string="Equipo", required=True)
    average_ids = fields.Many2many('res.partner', string="Objetivo Goles")
    scored_goals = fields.Float(string="Objetivo de goles", compute='_scored_goals')

    hours = fields.Float(string="Duration in hours",compute='_get_hours', inverse='_set_hours')

    @api.depends('goals', 'average_ids')
    def _scored_goals(self):
        for r in self:
            if not r.goals:
                r.scored_goals = 0.0
            else:
                r.scored_goals = 100.0 * len(r.average_ids) / r.goals


    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24