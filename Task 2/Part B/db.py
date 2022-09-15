import json
import logger

# The database file name
DB_FILE = "db.json"

# Read the database file and parse it as JSON
def read():
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except:
        logger.log_fatal("Database file not found for reading")

# Write the database file as JSON
def write(data):
    try:
        with open(DB_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except:
        logger.log_fatal("Database file not found for writing")

# Read the database file and return the specified key
def get(key):
    db = read()
    if db == None:
        return None

    return db[key]

# Set the specified key to the specified value and write the database file
def set(key, value):
    db = read()
    if db == None:
        return None

    db[key] = value
    write(db)
