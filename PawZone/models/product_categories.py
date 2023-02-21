from odoo import models,fields

class ProductCategories(models.Model):
    _name="product.categories"
    _description="Product Category"

    name=fields.Char(string="Category",required=True)
    
    active=fields.Boolean('Active',default=True)
    