{
    'name': 'Device Management',
    'author': 'Zaid Ansari',
    'summary': 'This is an Device management system',

    'depends' :['web','base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/device.xml',
        'views/device_assignment.xml',
        'views/device_attr_value.xml',
        'views/device_attribute_assignment.xml',
        'views/device_brand.xml',
        'views/device_attribute.xml',
        'views/device_type.xml',
    ],

    'installable': True,
    'application': True,

    'assets': {
        'web.assets_backend': [
           'device_management/static/src/**/*',
           ]
    },


}