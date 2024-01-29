from odoo import models, fields,api

class Employee(models.Model):
    _inherit = 'hr.employee'

    device_id = fields.One2many('device_management.device_assignment','employee_id',string="Device")