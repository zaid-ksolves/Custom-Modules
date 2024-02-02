# -*- coding: utf-8 -*-
from odoo import api, fields, models

class OwlTodo(models.Model):
    _name = 'person.list'
    _description = 'Person List App'

    name = fields.Char(string="Name")
    state = fields.Selection([('new', 'New'), ('approved', 'Approved')], string='State')


    def changeState(self):
        res = False
        for rec in self:
            if(rec.state=='new'):
                res = rec.write({'state':'approved'})
            else:
                res = rec.write({'state': 'new'})
        return res
