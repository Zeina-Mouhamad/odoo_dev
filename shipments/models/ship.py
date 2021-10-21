# -*- coding: utf-8 -*-

import base64
from random import choice
from string import digits
from werkzeug.urls import url_encode

# noinspection PyUnresolvedReferences
from odoo import api, fields, models, _
from odoo.osv.query import Query
from odoo.exceptions import ValidationError, AccessError
from odoo.modules.module import get_module_resource



class shipments(models.Model):
    _name = 'shipments.shipments'
    _description = 'shipments.shipments'

    #name = fields.Char(string='Vehicule')
    #vehicle_id = fields.Integer(string='Vehicle ID')
    #code = fields.Integer(string='Code', required=True)
    type = fields.Selection([('d2d', 'Door To Door'), ('b2b', 'Branch To Branch'), ('b2d', 'Branch To Door'), ('d2b', 'Door To Branch')], string='Type')
    date = fields.Date(string='Date')
    sender = fields.Many2one('res.partner', string="Sender")
    receiver = fields.Many2one('res.partner', string="Receiver")
    company = fields.Many2one('res.company', string=" Nearest Branch/Agent")
    weight = fields.Float(string='Weight')
    dimension = fields.Float(string='dimension')
    p_type = fields.Char(string='Payment Type')
    p_method = fields.Char(string='Payment Methods')
    from_address = fields.Char(string='From Address')
    to_address = fields.Char(string='To Address')
    specifications = fields.Selection([('breakable', 'Breakable'), ('cool', 'Keep in a cool place'), ('flammable', 'Flammable')], 'specifications')
    note = fields.Text(string='Description')
    expiry = fields.Boolean(string='expiry date')
    ex_date = fields.Date(string='Date')
    attachment_id = fields.Many2many('ir.attachment', 'attach_rel', 'doc_id', 'attach_id3', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)
    barcode = fields.Char(string="Barcode")
    #email_id = fields.Char(string="Email")

    class HrEmployeeAttachment(models.Model):
        _inherit = 'ir.attachment'

        attach_rel = fields.Many2many('hr.employee.document', 'doc_attachment_id', 'attach_id3', 'doc_id',
                                          string="Attachment", invisible=1)

    def action_send_email(self):
        template_id = self.env.ref('shipments.email_template_shipment').id
        template = self.env['mail.template'].browse(template_id)
        print("template", template)
        template.send_mail(self.id, force_send=True)

    @api.model
    def _default_image(self):
        image_path = get_module_resource('shipments', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    image = fields.Binary(string="Logo", attachment=True)
