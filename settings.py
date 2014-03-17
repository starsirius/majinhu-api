import os

# Running on local machine. Let's just use the local mongod instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'majinhu-admin'
MONGO_PASSWORD = 'majinhu2014'
MONGO_DBNAME = 'majinhu-api'
HATEOAS = False

# CORS
X_DOMAINS = '*'
X_HEADERS = 'Origin, X-Requested-With, Content-Type, Accept'

# let's not forget the API entry point (not really needed anyway)
#SERVER_NAME = '127.0.0.1:5000'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

users = {
    'datasource': {
        'projection': {'password': 0}
    },
    'schema': {
        'id': {
            'type': 'string',
            'minlength': 1
        },
        'email': {
            'type': 'string',
            'minlength': 4
        },
        'password': {
            'type': 'string',
            'minlength': 8
        },
        'role': {
            'type': 'string',
            'allowed': ["user", "admin"]
        }
    }
}

# Our API will expose two resources (MongoDB collections): 'artists' and
# 'artworks'. In order to allow for proper data validation, we define beaviour
# and structure.
artists = {
    # 'title' tag used in item links.
    'item_title': 'artist',

    # by default the standard item entry point is defined as
    # '/artists/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'id'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'id': {
            'type': 'string',
            'minlength': 1,
            'required': True,
            # talk about hard constraints! For the purpose of the demo
            # 'id' is an API entry-point, so we need it to be unique.
            'unique': True
        },
        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
            'required': True
        },
        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True
        },
        'year': {
            'type': 'dict',
            'schema': {
                'born': {
                    'type': 'datetime'
                },
                'died': {
                    'type': 'datetime'
                }
            }
        },
        'hometown': {
            'type': 'string'
        },
        'nationality': {
            'type': 'string'
        },
        'biography': {
            'type': 'dict',
            'schema': {
                'english': {
                    'type': 'string'
                },
                'chinese': {
                    'type': 'string'
                }
            }
        }
    }
}

artworks_schema = {
    'id': {
        'type': 'string',
        'required': True,
        'unique': True
    },
    'title': {
        'type': 'string',
        'required': True
    },
    'description': {
        'type': 'string'
    },
    'images': {
        'type': 'dict',
        'schema': {
            'image_versions': {
                'type': 'list',
                'allowed': ["small", "medium", "large", "original", "square"]
            },
            'image_url': {
                'type': 'string',
                'required': True
            }
        },
        'required': True
    },
    'owner': {
        'type': 'string',
        'required': True,
        # referential integrity constraint: value must exist in the
        # 'artists' collection. Since we aren't declaring a 'field' key,
        # will default to `artists._id` (or, more precisely, to whatever
        # ID_FIELD value is).
        'data_relation': {
            'resource': 'artists',
            'field': 'id'
        }
    },
    'width': {
        'type': 'number',
        'required': True
    },
    'height': {
        'type': 'number',
        'required': True
    },
    'category': {
        'type': 'list',
        'allowed': ["plum", "orchid", "bamboo", "mum", "wisteria", "peony", "grape", "lotus"]
    },
    'price': {
        'type': 'number'
    },
    'date': {
        'type': 'datetime',
        'required': True
    },
    'tags': {
        'type': 'list'
    }
}

artworks = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    #'item_title': 'artwork',

    # We choose to override global cache-control directives for this resource.
    #'cache_control': 'max-age=10,must-revalidate',
    #'cache_expires': 10,

    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'field': 'id'
    },

    'schema': artworks_schema
}

artist_artworks = {
    'url': 'artists/<regex("[\w-]+"):owner>/artworks',
    'datasource': { 'source': 'artworks' },
    'schema': artworks_schema
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'artists': artists,
    'artworks': artworks,
    'users': users,
    'artist_artworks': artist_artworks
}
