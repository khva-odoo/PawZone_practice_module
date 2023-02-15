from odoo import models, fields

class ProductDetails(models.Model):
    _name="product.details"
    _description="Product Details"

    name=fields.Char(required=True,)
    description=fields.Text()
    additional_information= fields.Text()
    vendor_price=fields.Float()
    sales_price=fields.Float()
    barcode=fields.Char()
    image=fields.Binary("Image", help="Select an appropriate image")
    quantity_on_hand=fields.Char()
    status=fields.Selection(
        string="Status",
        selection=[('available','Available'),('out_of_stock','Out-of-Stock')]
    )
    product_categories_id=fields.Many2one("product.categories", string="Product Category")