from odoo import models, fields, api


class international_Datasa(models.Model):
     _name = "specification"
     _description = "specification"


     name = fields.Char(string='name', required=True)
