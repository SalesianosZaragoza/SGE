# -*- coding: utf-8 -*-
{
    'name': "Asociación",

    'summary': """Weed club""",
    
    'description': """
        Module to manage soci:
    """,


    'author': "victor laguna",
    'website': "http://www.soci.weed",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'baseModule'],

    # always loaded
    'data': [
        'soci.xml',
        'security/ir.model.access.csv'
    ],
}
