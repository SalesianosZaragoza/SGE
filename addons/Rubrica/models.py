# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import timedelta,date,datetime

    
class carDealership(models.Model):
    _name = 'thefinalrubrica.cardealership'

    direction = fields.Char()
    workers_ids = fields.One2many('thefinalrubrica.worker', 'carDealership_id', string="Workers")
    tools_ids = fields.One2many('thefinalrubrica.tools', 'carDealership_id', string="Tools")
    vehicles_ids = fields.One2many('thefinalrubrica.vehicles', 'carDealership_id', string="Vehicles")

class tools(models.Model):
	_name = 'thefinalrubrica.tools'

	name = fields.Char()
	tool_type = fields.Char()
	carDealership_id = fields.Many2one('thefinalrubrica.cardealership', string="CarDealership")
	workers_ids = fields.Many2many(string= "WorkerTools" , comodel_name = 'thefinalrubrica.worker', relation = 'rel_workers_tools', column1='tools', column2='worker')


class vehicles(models.Model):
	_name = 'thefinalrubrica.vehicles'

	matricula = fields.Char()
	name = fields.Char()
	color = fields.Selection(selection=[('1', 'Blanco'), ('2', 'Gris'), ('3', 'Negro')])
	carDealership_id = fields.Many2one('thefinalrubrica.cardealership', string="CarDealership")
	worker_ids = fields.Many2many(string= "Something" , comodel_name = 'thefinalrubrica.worker', relation = 'rel_workers_vehicles', column1='vehicles', column2='worker')
	customers_id = fields.Many2one('thefinalrubrica.customers', string="Customers")

class worker(models.Model):
    _name = 'thefinalrubrica.worker'

    name = fields.Char()
    carDealership_id = fields.Many2one('thefinalrubrica.cardealership', string="CarDealership")
    vehicles_id = fields.Many2many(string= "Something" , comodel_name = 'thefinalrubrica.vehicles', relation = 'rel_workers_vehicles', column1='worker', column2='vehicles')
    tools_id = fields.Many2many(string= "WorkerTools" , comodel_name = 'thefinalrubrica.tools', relation = 'rel_workers_tools', column1='worker', column2='tools')
