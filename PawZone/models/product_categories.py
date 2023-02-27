from odoo import models,fields

class ProductCategories(models.Model):
    _name="product.categories"
    _description="Product Category"
    #_parent_name="parent_id"
    #_parent_store=True
    _order="name"

    name=fields.Char(string="Category",required=True)
   # parent_id=fields.Many2one('product.categories','Parent category')
   # child_ids=fields.One2many('product.categories','parent_id', 'Child category')
    
    active=fields.Boolean('Active',default=True)
    