{
    'name': 'School Management System',
    'author': 'Zaid Ansari',
    'website': 'www.schol.mngmt.com',
    'summary': 'This is an school management system',

    'depends':['base'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/notice_views.xml',
        'wizard/action_notice_view.xml',
        'wizard/update_student.xml',
        'data/cron.xml',
        'views/menu.xml',
        'views/student.xml',
        'views/school_views.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/student_record.xml',
        'views/school_class_views.xml',
        'views/subject_views.xml',
        'report/student_record.xml',
        'report/student_details.xml',

    ]
}
