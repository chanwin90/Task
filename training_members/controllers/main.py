from odoo import http
from odoo.http import request

class Members(http.Controller):

    @http.route('/member_webform', type="http", auth="public", website=True)
    def member_webform(self, **kwargs):
        return http.request.render('training_members.create_member',{})
    
    @http.route('/create/webmember', type='http', auth="public", website=True)
    def create_webmember(self, **kwargs):
        print("Data Received.......",kwargs)
        request.env['training_members.member'].sudo().create(kwargs)
        return request.render("training_members.member_thanks", {})