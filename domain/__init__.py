# -*- coding: utf-8 -*-
"""
  majinhu-api.domain
  ~~~~~~~~~~~

  this package exposes the API domain.

  :copyright: (c) 2014 by Chung-Yi Chi
  :license: 
"""
import apps, users, artists, artworks, artist_artworks

DOMAIN = {
  'apps': apps.definition,
  'users': users.definition,
  'artists': artists.definition,
  'artworks': artworks.definition,
  'artist_artworks': artist_artworks.definition
}
