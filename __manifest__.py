# -*- coding: utf-8 -*-
{
    'name': "Libra Loan",

    'summary': """
        Generacion de prestamos segun intereses, plazos, seguro, etc.""",

    'description': """
        Generacion de prestamos segun intereses, plazos, seguro, etc.
    """,

    'author': "Librasoft",
    'website': "https://libra-soft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','libra_base'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/libra_loan.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
