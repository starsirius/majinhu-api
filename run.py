import os, random, string
from eve import Eve

app = Eve()

def add_token(documents):
  # Don't use this in production:
  # You should at least make sure that the token is unique.
  for document in documents:
    document["token"] = (''.join(random.choice(string.ascii_uppercase)
      for x in range(10)))

if __name__ == '__main__':
  port = 5000
  host = '127.0.0.1'

  # create a token for each app on insertion
  #app.on_insert_apps += add_token
  app.run(host=host, port=port)
