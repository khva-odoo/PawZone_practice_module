from odoo import models,fields

class ProductCategories(models.Model):
    _name="product.categories"
    _description="Product Category"

    name=fields.Char(string="Category",required=True)
    #sub_name=fields.Char(string="Sub Category")
    active=fields.Boolean('Active',default=True)
    