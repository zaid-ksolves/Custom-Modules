from odoo import models, fields

class Subject(models.Model):
    _name = 'exams.subject'
    _description = 'Subject'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    exams_line = fields.One2many('exams.exam', 'subject_id', string='Exams')
