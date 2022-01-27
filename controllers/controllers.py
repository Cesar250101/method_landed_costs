# -*- coding: utf-8 -*-
from odoo import http

# class MethodLandedCosts(http.Controller):
#     @http.route('/method_landed_costs/method_landed_costs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_landed_costs/method_landed_costs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_landed_costs.listing', {
#             'root': '/method_landed_costs/method_landed_costs',
#             'objects': http.request.env['method_landed_costs.method_landed_costs'].search([]),
#         })

#     @http.route('/method_landed_costs/method_landed_costs/objects/<model("method_landed_costs.method_landed_costs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_landed_costs.object', {
#             'object': obj
#         })