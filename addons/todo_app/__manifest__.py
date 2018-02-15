{
    'name': 'To-Do Application',
    'description': 'Manage your personal Tasks with this module.',
    'author': 'Gorka Sanz',
    'depends': ['mail'],
    'data': ['todo_view.xml',
             'security/ir.model.access.csv',
             'security/todo_access_rules.xml', ],
    #Relacionamos con la vista
    'application': True,
}
