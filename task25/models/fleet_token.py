from odoo import models, fields

class FleetToken(models.Model):
    _name = 'custom_fleet.fleet_token'
    _description = 'Fleet Token'
    
    name = fields.Char(string='Token Name', required=True)
    car1 = fields.Many2one('fleet.vehicle',string='Car')
    