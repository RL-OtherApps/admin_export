# -*- coding: utf-8 -*-
{
    'name': 'Remove Export Option',
    'description': 'Remove the \'Export\' option from the \'More\' menu...',
    'version': '1.0',
    'author': '',
    'website': '',
    'images': ['static/description/main_screenshot.png'],
    'category': 'Web',
    'description': """
""",
    'depends': ['web'],
    'data': [
        'security/export_visible_security.xml',
        'view/disable_export_view.xml',
    ],
    'auto_install': False,
}
