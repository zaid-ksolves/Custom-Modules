{
    'name': 'School Extends',
    'author': 'Zaid Ansari',
    # 'website': 'www.schol.mngmt.com',
    'summary': 'This is an school extended management system',

    'depends':['base','school'],

    'installable': True,
    'application': True,

    'data': [
        'views/student_profile.xml',
    ]
}
