# -*- coding: utf-8 -*-
from odoo import api, fields, models

class TaskInherited(models.Model):
    _inherit = 'project.task'
    _description = "Inherited Project Model"

    sales = fields.One2many('sale.order','task_id',string="Sales")

    def sales_records(self):
        return {
            'name': 'Linked Sale Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.sales.ids)],
        }
    def open_so_wiz(self):
        return{
            'name': 'Linked Sale Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.wizard',
            'view_mode': 'form',
            'target': 'new',
            'view_id': False,
            'context': {'default_task_id': self.id }
        }
