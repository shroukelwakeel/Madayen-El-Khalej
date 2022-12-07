# -*- coding: utf-8 -*-
{
    'name': "Saudi Vat Invoice Simplified One",
    'summary': """Saudi Vat Invoice Simplified""",
    'description': """Helps to generate Simplified""",
    'version': '14.0.1.0.0',
    'category': 'Accounting',
    'author': "6Sigmacode",
    'website': "",
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'account', 'saudi_vat_invoice', '6sigmacode_saudi_vat_invoice', 'sa_uae_vat'],
    'qweb': [],
    'data': [
         'views/view.xml',
         'report/report_paperformat.xml',
         'report/header.xml',
         # 'report/report.xml',
         'report/report_simplified.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
