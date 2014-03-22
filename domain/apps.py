# -*- coding: utf-8 -*-
"""
  majinhu-api.domain.apps.py
  ~~~~~~~~~~~~~~~~~~~~~~~

  'apps' resource and schema settings.

  :copyright: (c) 2013 by Chung-Yi Chi
  :license:
"""

from auth import BasicAuth

definition = {
  'authentication': BasicAuth(),

  # We also disable endpoint caching as we don't want client apps to
  # cache app data.
  'cache_control': '',
  'cache_expires': 0,

  'datasource': {
    'projection': {'token': 1}
  },
  'schema': {
    'id': {
      'type': 'string',
      'minlength': 8,
      'required': True
    },
    'secret': {
      'type': 'string',
      'minlength': 8,
      'required': True
    },
    'token': {
      'type': 'string',
      'minlength': 8,
      'required': True
    }
  }
}
