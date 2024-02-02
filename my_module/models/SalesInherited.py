# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SalesInherited(models.Model):
    _inherit = 'sale.order'
    _description = "Inherited Sales Model"

    task_id = fields.Many2one('project.task',string="Task")

    def save_manually(self):
        return True




