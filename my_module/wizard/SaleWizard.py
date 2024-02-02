
from odoo import api, fields, models, _

class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'

    sale_order_id = fields.Many2many('sale.order', string="Sale Orders")

    name = fields.Char(string="SO Name")
    partner_id = fields.Many2one('res.partner', string="Customer")
    user_id = fields.Many2one('res.users', string="Salesperson")

    def action_save(self):
        active_id = self.env.context.get('default_task_id')
        for rec in self:
            rec.sale_order_id.task_id = active_id
