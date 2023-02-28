from odoo import models,fields

class ResUsers(models.Model):
    _name="res.users"
    _description="Customer Details"
    _inherit="res.users"

    # name=fields.Char(required=True)
    # email_id=fields.Char()
    # phone_number=fields.Char()
    # address=fields.Text()
    # city=fields.Char()
    # state_id = fields.Many2one('res.country.state', string='States',domain="[('country_id','=?',country_id)]")
    # country_id=fields.Many2one('res.country',string='Country')
    # pincode=fields.Char()
    # image=fields.Binary()
    # active=fields.Boolean('Active',default=True)

