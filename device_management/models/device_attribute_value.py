from odoo import models, fields,api

class DeviceAttributeValue(models.Model):
    _name = 'device_management.device_attr_value'
    _description = 'Device Attribute Value'

    name = fields.Char(string="Name")
    device_attribute_id = fields.Many2one('device_management.device_attribute',string="Device Attribute")

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another Name - it has to be unique!')
    ]
