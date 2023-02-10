from odoo import models,fields

class CustomerDetails(models.Model):
    _name="customer.details"
    _description="Customer Details"


    name=fields.Char()
    email_id=fields.Char()
    phone_number=fields.Integer()
    address=fields.Text()
    city=fields.Char()
    state=fields.Char()
    country=fields.Char()
    pincode=fields.Integer()


