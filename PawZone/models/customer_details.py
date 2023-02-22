from odoo import models,fields

class CustomerDetails(models.Model):
    _name="customer.details"
    _description="Customer Details"


    name=fields.Char(required=True)
    email_id=fields.Char()
    phone_number=fields.Char()
    address=fields.Text()
    city=fields.Char()
    state_id = fields.Many2one('res.country.state', string='States',domain="[('country_id','=?',country_id)]")
    country_id=fields.Many2one('res.country',string='Country')
    pincode=fields.Char()
    image=fields.Binary()
    active=fields.Boolean('Active',default=True)

