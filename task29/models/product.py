from odoo import fields,models,api

class ProductInherit(models.Model):
    _inherit = 'product.product'
    internal_reference = fields.Char(string='Internal Reference')

    @api.onchange('default_code')
    def _onchange_default_code(self):
            if not self.default_code:
                return

            domain = [('default_code', '=', self.default_code)]
            if self.id.origin:
                domain.append(('id', '!=', self.id.origin))

            if self.env['product.product'].search(domain, limit=1):
                return {'warning': {
                    'title': _("Note:"),
                    'message': _("The Internal Reference '%s' already exists.", self.default_code),
                }}
            