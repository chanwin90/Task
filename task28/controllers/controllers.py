# -*- coding: utf-8 -*-
# from odoo import http


# class Task28(http.Controller):
#     @http.route('/task28/task28', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task28/task28/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task28.listing', {
#             'root': '/task28/task28',
#             'objects': http.request.env['task28.task28'].search([]),
#         })

#     @http.route('/task28/task28/objects/<model("task28.task28"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task28.object', {
#             'object': obj
#         })
