import os
from eve import Eve

app = Eve()

if __name__ == '__main__':
    port = 5000
    host = '127.0.0.1'

    app.run(host=host, port=port)
