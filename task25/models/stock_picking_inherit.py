from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    fleet_token_ids = fields.Many2one('custom_fleet.fleet_token', string='Fleet token')
    car1 = fields.Many2one(related='fleet_token_ids.car1',string='Car')
    
        
    @api.onchange('fleet_token_ids')
    def _onchange_fleet_token(self):
        if self.fleet_token_ids:
            self.car1 = self.fleet_token_ids.car1  # Update the car1 field
            return {'domain': {'car1': [('id', '=', self.fleet_token_ids.car1.id)]}}
        else:
            self.car1 = None  # Reset the car1 field
            return {'domain': {'car1': []}}
