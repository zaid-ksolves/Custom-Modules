from odoo import models, fields,api

class DeviceBrand(models.Model):
    _name = 'device_management.device_brand'
    _description = 'Device Brand'

    name = fields.Char(string="Name")
    device_model_line = fields.One2many('device_management.device_model','device_brand_id',string="Device Model")

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Choose another Name - it has to be unique!')
    ]