DEBUG = [True]

RESOURCE_METHODS = ['GET','POST','DELETE']

#ITEM_METHODS = ['GET','PATCH','DELETE']

DOMAIN = {
    'foto': {
        'additional_lookup':
            {
                'url': 'regex("[\w]+")',
                'field': 'titulo'
            },
        'schema': {
            'titulo': {
                'type': 'string',
                'unique': True
            },
            'url': {
                'type': 'media'
            }
        }
    }

}

