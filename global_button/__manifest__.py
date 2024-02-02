# -*- coding: utf-8 -*-

{
    'name': 'Global Button',
    'version': '1.0',
    'summary': 'Global Button',
    'description': """Global Button""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/global_button.xml'
    ],

    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'global_button/static/src/components/todo_list/js/global.js',
            'global_button/static/src/components/todo_list/xml/todo_list.xml',
        ],
    },
}
