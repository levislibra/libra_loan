# -*- coding: utf-8 -*-
# from odoo import http


# class LibraPrestamos(http.Controller):
#     @http.route('/libra_prestamos/libra_prestamos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libra_prestamos/libra_prestamos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libra_prestamos.listing', {
#             'root': '/libra_prestamos/libra_prestamos',
#             'objects': http.request.env['libra_prestamos.libra_prestamos'].search([]),
#         })

#     @http.route('/libra_prestamos/libra_prestamos/objects/<model("libra_prestamos.libra_prestamos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libra_prestamos.object', {
#             'object': obj
#         })
