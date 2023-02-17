from odoo import models,fields

class PetInformation(models.Model):
    _name = "pet.information"
    _description = "All information regarding pet"
    _rec_name="pet_id"

    pet_id = fields.Char(string = 'Pet Id',required=True,)
    pet_description = fields.Text()
    pet_gender = fields.Selection(
        string = 'Gender',
        selection = [('M', 'Male'),('F','Female')],
        help='Select gender'
    )
    pet_type = fields.Char()
    
    pet_status = fields.Selection(
        string = 'Status',
        selection = [('available','Available'), ('not_available','Not Available')]
    )
    active=fields.Boolean('Active',default=True)
    pet_birth_date = fields.Date(string="Date of Birth")
    image=fields.Binary("Image",help="Select image here",)
    
    pet_category_id = fields.Many2one("pet.category", string = "Pet Category")
    pet_breeds_id=fields.Many2one("pet.breeds",string="Breed")
    vendor_id=fields.Many2one("vendor.details",string="Vendor")