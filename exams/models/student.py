from odoo import models, fields

class Student(models.Model):
    _name = 'exams.student'
    _description = 'Student'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    address = fields.Text(string='Address')
    exams_line = fields.One2many('exams.exam', 'student_id', string='Exams')
