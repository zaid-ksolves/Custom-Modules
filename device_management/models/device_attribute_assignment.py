from odoo import models, fields,api

class DeviceAttrAssignment(models.Model):
    _name = 'device_management.device_attr_assignment'
    _description = 'Device Attribute Assignment'

    device_id = fields.Many2one('device_management.device',string="Device")
    device_attribute_id = fields.Many2one('device_management.device_attribute',string = "Device Attribute")
    device_attribute_value_id = fields.Many2one('device_management.device_attr_value',string="Device Attribute Value")