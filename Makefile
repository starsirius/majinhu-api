DB_NAME = majinhu-api
DB_USER = majinhu-admin

NOW := $(shell date +%b_%d_%Y_%H_%M_%S)
DB_BACKUP_DEST = ./data/backup/db_backup_$(NOW) # destination folder

DB_COLS = users artists artworks client_apps
DB_DATA_DIR = ./data

# Start the api
s:
	source ./venv/bin/activate && python run.py

# Backup database
db-backup:
	mkdir -p $(DB_BACKUP_DEST)
#        Use --oplog if MongoDB is running as a replica set
#	http://stackoverflow.com/questions/17458124/how-to-get-a-consistent-mongodb-backup-for-a-single-node-setup
#	mongodump --db $(DB_NAME) --oplog --out $(DB_BACKUP_DEST) --username $(DB_USER) --password
	mongodump --db $(DB_NAME) --out $(DB_BACKUP_DEST) --username $(DB_USER) --password

# Initialize database (this will backup the database, drop all the collections, and initialize data)
db-init: db-backup
	$(foreach col, $(DB_COLS), \
	  mongo $(DB_NAME) --eval "db.$(col).drop()"; \
	  mongoimport --db $(DB_NAME) --collection $(col) --type json --file data/init_$(col).json --jsonArray; \
	)
