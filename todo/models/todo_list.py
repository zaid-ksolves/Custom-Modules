# -*- coding: utf-8 -*-
from odoo import api, fields, models

class OwlTodo(models.Model):
    _name = 'todo.todo.list'
    _description = 'TODO Todo List App'

    name = fields.Char(string="Task Name")
    completed = fields.Boolean()
    color = fields.Char()
