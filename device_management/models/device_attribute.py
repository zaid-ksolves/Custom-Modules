from odoo import models, fields,api

class DeviceAttribute(models.Model):
    _name = 'device_management.device_attribute'
    _description = 'Device attribute'

    name = fields.Char(string="Name")
    device_type_id = fields.Many2one('device_management.device_type',string="Device Type")
    required = fields.Boolean(string="Required")
    device_attribute_value_line = fields.One2many('device_management.device_attr_value','device_attribute_id',string="Device Attribute Value")

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another Name - it has to be unique!')
    ]
