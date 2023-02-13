from odoo import models, fields

class ProductDetails(models.Model):
    _name="product.details"
    _description="Product Details"

    name=fields.Char(required=True, string="Product Name")
    description=fields.Text()
    additional_information= fields.Text()
    sales_price=fields.Float()
    barcode=fields.Char()
    image=fields.Binary(default=True, string="Image", help="select image here")

    