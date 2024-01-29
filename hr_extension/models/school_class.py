from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'hr_extension.school_class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)
    teacher_ids = fields.Many2many('hr_extension.teacher', string='Teachers')