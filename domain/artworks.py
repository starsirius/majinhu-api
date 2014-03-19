# -*- coding: utf-8 -*-
"""
  majinhu-api.domain.artworks.py
  ~~~~~~~~~~~~~~~~~~~~~~~

  'artworks' resource and schema settings.

  :copyright: (c) 2013 by Chung-Yi Chi
  :license:
"""

_schema = {
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

definition = {
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

    'schema': _schema
}
