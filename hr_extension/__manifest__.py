{
    'name': 'Hr Extended',
    'author': 'Zaid Ansari',
    'summary': 'This is Hr extended module',

    'depends': ['base', 'hr'],

    'installable': True,
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/class_view.xml',
        'views/teacher_view.xml',
    ]
}
