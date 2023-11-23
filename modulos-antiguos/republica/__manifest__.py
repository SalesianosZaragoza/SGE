# -*- coding: utf-8 -*-
{
    'name': "Republica",

    'summary': """Republica always win""",
    
    'description': """
        Module to manage republica:
    """,


    'author': "Jose Luis Gardeta",
    'website': "http://www.jedi.republica",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'baseModule'],

    # always loaded
    'data': [
        'republica.xml',
        'security/ir.model.access.csv'
    ],
}
