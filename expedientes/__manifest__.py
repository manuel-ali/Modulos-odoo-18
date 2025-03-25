{
    'name': 'Expedientes',
    'version': '2.0',
    'author': 'prueba',
    'category': 'AbogadosAsociados',
    'description': 'Modulo de Expedientes permite la gestión de ellos.',
    'summary': 'Estamos ante el módulo más grande y complejo de todo nuestro trabajo donde se juntan varias relaciones, entre Abogados, diferentes Documentos, Trámites y Clientes.',
    
    'application': True,
    'installable': True,
    'data': [
        'views/festivo_views.xml',
        'views/expediente.xml',
        'views/tramites_views.xml',
        'views/views.xml',
        'security.xml',
        'sequence.xml'
    ],
    'icon': '/expedientes/static/description/icon.png',
    'depends': ['base', 'Clientes', 'Abogados', 'Juzgados', 'Aseguradoras']
}
