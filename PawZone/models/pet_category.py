from odoo import models,fields

class PetCategory(models.Model):
    _name = "pet.category"
    _description = "Pet Category"

    name = fields.Char(required=True, string="Category",help="Which category does the pet belongs to")   
    active=fields.Boolean('Active',default=True)