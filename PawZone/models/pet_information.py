from odoo import models,fields,api
from datetime import datetime
from dateutil.relativedelta import relativedelta 
from odoo.exceptions import UserError

class PetInformation(models.Model):
    _name = "pet.information"
    _description = "All information regarding pet"
    _rec_name="pet_id"

    
    pet_id = fields.Char(string = 'Pet Id',required=True,)
    sequence = fields.Integer(default=1)
    pet_description = fields.Text()
    pet_gender = fields.Selection(
        string = 'Gender',
        selection = [('M', 'Male'),('F','Female')],
        help='Select gender'
    )
    pet_type = fields.Char()
    
    pet_status = fields.Selection(
        string = 'Status',
        selection = [('available','Available'),('sold','Sold'),('canceled','Canceled')],
        required=True,
        copy=False,
        default="available"
    )
    active=fields.Boolean('Active',default=True)
    pet_birth_date = fields.Date(string="Date of Birth",default=datetime.date(datetime.today()) )
    image=fields.Binary("Image",help="Select image here",)
    
    pet_category_id = fields.Many2one("pet.category", string = "Pet Category")
    pet_breeds_id=fields.Many2one("pet.breeds",string="Breed",domain="[('category_id','=?',pet_category_id)]")
    vendor_id=fields.Many2one("vendor.details",string="Vendor")
    vendor_price=fields.Float()
    sales_price=fields.Float()
    pet_age=fields.Integer(string="Age(days)", compute="_compute_pet_age",inverse="_inverse_pet_age",store=True)
   

    _sql_constraints=[
        ('pet_id_unique','unique(pet_id)','ID already exists'),
        ('check_vendor_price','CHECK(vendor_price>0)','Price must br greater than 0'),
        ('check_sales_price','CHECK(sales_price>0)','Price must be greater than 0')
    ]

    @api.depends ('pet_birth_date')
    def _compute_pet_age(self):
        for record in self:
            if (record.pet_birth_date<=fields.Date.today()):
                record.pet_age=(fields.Date.today()-record.pet_birth_date).days
            else:
                record.pet_age="0"

    def _inverse_pet_age(self):
        for record in self:
            if (record.pet_age>0):
                record.pet_birth_date=(fields.Date.today()-relativedelta(days=record.pet_age))
            else:
                record.pet_birth_date=fields.Date.today()

    def action_sold(self):
        for record in self:
            if record.pet_status=="canceled":
                raise UserError("Cannot be sold")
            else:
                record.pet_status="sold"
            return True
        
    def action_cancel(self):
        for record in self:
            if record.pet_status=="sold":
                raise UserError("Cannot be canceled")
            else:
                record.pet_status="canceled"
            return True
        
        
    