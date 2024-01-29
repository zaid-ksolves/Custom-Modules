from odoo import models, fields,api

class Exam(models.Model):
    _name = 'exams.exam'
    _description = 'Exam Marks'

    student_id = fields.Many2one('exams.student', string='Student', required=True)
    subject_id = fields.Many2one('exams.subject', string='Subject', required=True)
    marks = fields.Float(string='Marks')
    exam_date = fields.Date(string='Exam Date')
    grade = fields.Char(string='Grade')

    @api.model
    def perform_action(self):
        print("Hello")

