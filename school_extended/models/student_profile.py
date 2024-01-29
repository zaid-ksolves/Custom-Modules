from odoo import fields,models

class student_profile(models.Model):
    _inherit='school.student'

    student_father_name = fields.Char("Father Name")