from odoo import models, fields,api

class DeviceAssignment(models.Model):
    _name = 'device_management.device_assignment'
    _description = 'Device Assignment'

    name = fields.Char(string="Name")
    device_id = fields.Many2one('device_management.device',string="Device")
    employee_id = fields.Many2one('hr.employee',string="Employee")
    date_start = fields.Date(string="Start Date")
    date_expire = fields.Date(string="Expriry Date")
    state = fields.Selection([
        ('new', 'New'),
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected')],
        string="State")