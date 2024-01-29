{
    'name': 'Dual Database',
    'author': 'Zaid Ansari',
    'summary': 'This is dual database',

    'depends' :['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/person.xml',
    ],

    'installable': True,
    'application': True,



}