{
    'name': "PawZone",
    'version': '1.0',
    'depends': ['base','sale_management'],
    'author': "Author Name",
    'category': 'Category',
    'license': 'LGPL-3',
    
    'description': """
    Description text
    """,

    'data':[
        'security/ir.model.access.csv',
        'views/pet_category_views.xml',
        'views/product_views.xml',
        'views/pet_information_views.xml',
        'views/res_users_views.xml',
        'views/product_details_views.xml',
        'views/product_categories_views.xml',
        'views/pet_services_views.xml',
        'views/vendor_details_views.xml',
        'views/pet_breeds_views.xml',
        'views/PawZone_menus.xml',
        
        
        
        
    ],

    'application': True,
    'installable': True,
} 