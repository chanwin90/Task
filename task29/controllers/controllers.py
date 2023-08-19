# -*- coding: utf-8 -*-
# from odoo import http


# class Task29(http.Controller):
#     @http.route('/task29/task29', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task29/task29/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task29.listing', {
#             'root': '/task29/task29',
#             'objects': http.request.env['task29.task29'].search([]),
#         })

#     @http.route('/task29/task29/objects/<model("task29.task29"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task29.object', {
#             'object': obj
#         })
