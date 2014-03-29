majinhu-api
===========

Ma Jinhu website api

## Development

### Install and run MongoDB
##### Install [MongoDB](http://docs.mongodb.org/manual/installation/)
##### Run [MongoDB](http://docs.mongodb.org/manual/tutorial/manage-mongodb-processes/)
##### Configure production envirionment
Use the `settings.prod.py.example` as an example to configure your production environment, and export `EVE_SETTINGS` environment variable to point to the file. See more details in the Eve [Development / Production](http://python-eve.org/config.html#development-production).
```bash
cp settings.prod.py.example setting.prod.py
vim setting.prod.py # Or whatever editor to modify the prod settings
export EVE_SETTINGS=/path/to/setting.prod.py
```
##### Add a admin user to the database
Here is an example. In the mongo shell:
```
use majinhu-api
db.addUser( { user: "majinhu-admin", pwd: "password", roles: [ "readWrite", "dbAdmin" ]} )
```
##### Initialize some data
```bash
make db-init
```

### Install Python and Python-dev
 - Install Python
 - Install Python-dev which is needed to compile bcrypt: `sudo apt-get install python-dev`

### Install pip
 - On ubuntu, `sudo apt-get install python-pip`. See the [doc](http://pip.readthedocs.org/en/latest/installing.html) for installation on other platforms.

### Install virtualenv
```bash
sudo pip install virtualenv
```

### Run bootstrap.sh
```bash
bash bootstrap.sh
```

### Run the app
```bash
make s
```
