# -*- coding: utf-8 -*-

{
    'name' : 'Test App',
    'version' : '1.0',
    'summary': 'Test App',
    'description': """Todo App""",
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'todo/static/src/components/todo_list/js/new_todo.js',
            'todo/static/src/components/todo_list/xml/todo_list.xml',
        ],
    },
}
