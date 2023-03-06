from odoo import models,fields

class ProductProduct(models.Model):
    _name="product.template"
    _inherit="product.template"

    vendor_ids=fields.Many2many("vendor.details",string=" Vendor Information")