# -*- coding: utf-8 -*-
"""
  majinhu-api.domain.artist_artworks.py
  ~~~~~~~~~~~~~~~~~~~~~~~

  'artist_artworks' resource and schema settings.

  :copyright: (c) 2013 by Chung-Yi Chi
  :license:
"""

import artworks

definition = {
    'url': 'artists/<regex("[\w-]+"):owner>/artworks',
    'datasource': { 'source': 'artworks' },
    'schema': artworks._schema
}


