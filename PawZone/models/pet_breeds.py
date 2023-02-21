from odoo import models,fields

class PetBreeds(models.Model):
    _name = "pet.breeds"
    _description = "Pet Breeds"

    name = fields.Char(required=True,string="Breed",help = "Choose which breed the pet belongs to?")  
    description=fields.Text() 
    active=fields.Boolean('Active',default=True)

    vendor_ids=fields.Many2many("vendor.details",string="Vendors")
    