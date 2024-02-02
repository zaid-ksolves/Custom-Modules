{
    'name': 'My module',
    'author': 'Zaid Ansari',
    'summary': 'Module',

    'depends': ['base', 'project','sale'],

    'installable': True,
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'views/task.xml',
        'views/sale_view.xml',
        'wizard/SaleWizardView.xml',
    ]
}
