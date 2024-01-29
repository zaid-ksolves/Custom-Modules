from odoo import models, fields,api

class Device(models.Model):
    _name = 'device_management.device'
    _description = 'Device'

    name = fields.Char(string="Name")
    shared = fields.Boolean(string="is shared ?")
    device_type_id = fields.Many2one('device_management.device_type', string="Device Type")
    device_brand_id = fields.Many2one('device_management.device_brand',string="Device Brand")
    device_model_id = fields.Many2one('device_management.device_model',string="Device Model")
    attributes_line = fields.One2many('device_management.device_attr_assignment','device_id',string="Attributes")