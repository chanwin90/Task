# -*- coding: utf-8 -*-
# from odoo import http


# class Task25(http.Controller):
#     @http.route('/task25/task25', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task25/task25/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task25.listing', {
#             'root': '/task25/task25',
#             'objects': http.request.env['task25.task25'].search([]),
#         })

#     @http.route('/task25/task25/objects/<model("task25.task25"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task25.object', {
#             'object': obj
#         })
