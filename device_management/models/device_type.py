from odoo import models, fields,api

class DeviceType(models.Model):
    _name = 'device_management.device_type'
    _description = 'Device Type'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    sequence = fields.Char(string='Sequence', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('device_management_device_type_seq'))
    device_attribute_line = fields.One2many('device_management.device_attribute','device_type_id',string="Device Attribute")
    device_model_line = fields.One2many('device_management.device_model','device_type_id',string="Device Model")
    device_line = fields.One2many('device_management.device','device_type_id',string="Device")

    _sql_constraints = [
        ('code_unique',
         'unique(code)',
         'Choose another code - it has to be unique!')
    ]