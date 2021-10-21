# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Shipments(http.Controller):
    @http.route('/shipment_webform', type='http', auth='user', website=True)
    def shipment_webform(self, **kw):
        shipment_rec = request.env['shipments.shipments'].sudo().search([])
        return http.request.render('shipments.create_shipment', {})

    @http.route('/create/webshipment', type='http', auth='public', website=True)
    def create_webshipment(self, **kw):
        request.env['shipments.shipments'].sudo().create(kw)
        return request.render("shipments.shipment_thanks", {})
