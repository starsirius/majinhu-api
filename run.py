import os
import bcrypt
from eve import Eve
from eve.auth import BasicAuth

class BCryptAuth(BasicAuth):
  def check_auth(self, username, password, allowed_roles, resource, method):
    # use Eve's own db driver; no additional connections/resources are used
    users = app.data.driver.db['users']
    lookup = {'username': username}
    if allowed_roles:
      # only retrieve a user if his roles match ``allowed_roles``
      lookup['roles'] = {'$in': allowed_roles}
    user = users.find_one(lookup)
    return user and bcrypt.hashpw(password, user['password']) == user['password']

app = Eve(auth=BCryptAuth)

if __name__ == '__main__':
    port = 5000
    host = '127.0.0.1'

    app.run(host=host, port=port)
