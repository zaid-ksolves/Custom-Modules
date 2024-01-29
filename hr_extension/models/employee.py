from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean(string='Is a Teacher')
    classes_line = fields.Many2many('teacher_management.school_class', string='Classes Taught')