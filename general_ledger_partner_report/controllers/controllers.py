# -*- coding: utf-8 -*-
# from odoo import http


# class GeneralLedgerPartnerReport(http.Controller):
#     @http.route('/general_ledger_partner_report/general_ledger_partner_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/general_ledger_partner_report/general_ledger_partner_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('general_ledger_partner_report.listing', {
#             'root': '/general_ledger_partner_report/general_ledger_partner_report',
#             'objects': http.request.env['general_ledger_partner_report.general_ledger_partner_report'].search([]),
#         })

#     @http.route('/general_ledger_partner_report/general_ledger_partner_report/objects/<model("general_ledger_partner_report.general_ledger_partner_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('general_ledger_partner_report.object', {
#             'object': obj
#         })
