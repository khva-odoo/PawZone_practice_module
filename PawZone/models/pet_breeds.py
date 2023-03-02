from odoo import models,fields,api

class PetBreeds(models.Model):
    _name = "pet.breeds"
    _description = "Pet Breeds"
    _order="name"

    name = fields.Char(required=True,string="Breed",help = "Choose which breed the pet belongs to?")  
    description=fields.Text() 
    active=fields.Boolean('Active',default=True)
    category_id=fields.Many2one("pet.category",string="Category",required=True)
    vendor_ids=fields.Many2many("vendor.details",string="Vendors")
    pet_ids=fields.One2many(
        comodel_name="pet.information",
        inverse_name="pet_breeds_id")
    pet_count=fields.Integer(compute="_compute_pet_count")
    

    @api.depends('pet_ids')
    def _compute_pet_count(self):
        for record in self:
            record.pet_count=len(record.pet_ids)
