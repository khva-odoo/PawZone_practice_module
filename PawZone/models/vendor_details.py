from odoo import models,fields

class VendorDetails(models.Model):
    _name="vendor.details"
    _description="Vendor Details"
    
    name=fields.Char(string="Name")
    company_name=fields.Char()
    address=fields.Text()
    city=fields.Char()
    state=fields.Char()
    country=fields.Char()
    phone=fields.Char(string="Phone")
    email=fields.Char()
    website=fields.Char()
    image=fields.Binary()
    notes=fields.Text()
    breeds_ids=fields.Many2many("pet.breeds",string="Breeds")
    pet_ids=fields.One2many(
        comodel_name="pet.information",
        inverse_name="vendor_id"
        )
    product_ids=fields.Many2many("product.details",string="Products")
    service_ids=fields.Many2many("pet.services",string="Services")