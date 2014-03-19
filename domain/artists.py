# -*- coding: utf-8 -*-
"""
  majinhu-api.domain.artists.py
  ~~~~~~~~~~~~~~~~~~~~~~~

  'artists' resource and schema settings.

  :copyright: (c) 2013 by Chung-Yi Chi
  :license:
"""

definition = {
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
