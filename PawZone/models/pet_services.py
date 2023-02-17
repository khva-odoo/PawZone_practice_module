from odoo import models,fields

class PetServices(models.Model):
    _name="pet.services"
    _description="Pet Services"

    name=fields.Char(required=True,string="Service Name")
    type=fields.Selection(
        string="Service Type",
        selection=[('grooming','Grooming'),('hostel','Hostel')]
    )
    fees=fields.Char()
    service_detail=fields.Text(string="Service Detail")
    active=fields.Boolean('Active',default=True)
    vendor_ids=fields.Many2many("vendor.details",string="Vendor")