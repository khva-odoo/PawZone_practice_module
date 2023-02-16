from odoo import models,fields

class CustomerDetails(models.Model):
    _name="customer.details"
    _description="Customer Details"


    name=fields.Char(required=True)
    email_id=fields.Char()
    phone_number=fields.Char()
    address=fields.Text()
    city=fields.Char()
    state=fields.Char()
    country=fields.Char()
    pincode=fields.Char()
    image=fields.Binary()
    active=fields.Boolean('Active',default=True)

