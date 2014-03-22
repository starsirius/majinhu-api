import bcrypt
from flask import current_app as app
from eve.auth import BasicAuth, TokenAuth

class BasicAuth(BasicAuth):
  def check_auth(self, username, password, allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
    apps = app.data.driver.db['apps']
    lookup = {'id': username, 'secret': password}
    return apps.find_one(lookup)

class BCryptAuth(BasicAuth):
  def check_auth(self, username, password, allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
    users = app.data.driver.db['users']
    lookup = {'username': username}
    if allowed_roles:
      # only retrieve a user if his roles match `allowed_roles`
      lookup['roles'] = {'$in': allowed_roles}
    user = users.find_one(lookup)
    return user and bcrypt.hashpw(password, user['password']) == user['password']

class AppTokenAuth(TokenAuth):
  def check_auth(self, token,  allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
    accounts = app.data.driver.db['apps']
    lookup = {'token': token}
    return apps.find_one(lookup)
