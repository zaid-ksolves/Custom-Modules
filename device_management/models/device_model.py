from odoo import models, fields,api

class DeviceModel(models.Model):
    _name = 'device_management.device_model'
    _description = 'Device Model'

    device_type_id = fields.Many2one('device_management.device_type',string="Device Type")
    device_brand_id = fields.Many2one('device_management.device_brand', string="Device Brand")