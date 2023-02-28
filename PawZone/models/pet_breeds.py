from odoo import models,fields

class PetBreeds(models.Model):
    _name = "pet.breeds"
    _description = "Pet Breeds"
    _order="name"

    name = fields.Char(required=True,string="Breed",help = "Choose which breed the pet belongs to?")  
    description=fields.Text() 
    active=fields.Boolean('Active',default=True)
    category_id=fields.Many2one("pet.category",string="Category")
    vendor_ids=fields.Many2many("vendor.details",string="Vendors")
    pet_ids=fields.One2many("pet_information","pet_breeds_id")
    pet_count=fields.Integer(compute="__compute_pet_count")


