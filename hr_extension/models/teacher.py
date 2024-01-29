from odoo import models, fields

class Teacher(models.Model):
    _name = 'hr_extension.teacher'
    _description = 'Teacher Information'

    name = fields.Char(string='Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee')
    class_ids = fields.Many2many('hr_extension.school_class', string='Classes')