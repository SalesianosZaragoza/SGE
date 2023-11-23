# -*- coding: utf-8 -*-
{
    'name': "Teatro",
    'summary': """Gestión de teatro""",
    'description': """
        Aplicación de un teatro, sus salas, películas, promociones...
    """,
    'author': "Pablo Villarte",
    'website': "https://github.com/pvillarte",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}