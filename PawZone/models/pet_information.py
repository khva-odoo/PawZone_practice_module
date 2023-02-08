from odoo import models,fields

class PetInformation(models.Model):
    _name = "pet.information"
    _description = "All information regarding pet"

    pet_id = fields.Integer(string = 'Pet Id',required=True)
    pet_description = fields.Text(required=True)
    pet_gender = fields.Selection(
        string = 'Gender',
        selection = [('M', 'Male'),('F','Female')],
        help='Select gender'
    )
    pet_status = fields.Selection(
        string = 'Status',
        selection = [('sold','Sold'), ('unsold','Unsold')]
    )
    price = fields.Float(required=True)
