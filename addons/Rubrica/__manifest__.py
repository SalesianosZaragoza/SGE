# -*- coding: utf-8 -*-
{
    'name': "rubrica",

    'summary': """modulo de rubrica""",

    'description': """
        modulo rubrica
    """,

    'author': "G sanz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'view.xml',
    ],

}