import db
import uuid

# Reads the database file and returns the users key
def get_users():
    return db.get("users")

# Gets the specified user from the database based on ID
def get_user(uid):
    users = get_users()
    if users == None:
        return None

    for user in users:
        if str(user["id"]) == str(uid):
            return user

    return None

# Gets the specified user from the database based on name
def get_user_by_name(name):
    users = get_users()
    if users == None:
        return None

    for user in users:
        if user["name"] == name:
            return user

    return None

# Checks if the specified user is a staff member
def is_staff(uid):
    user = get_user(uid)
    if user == None:
        return False

    return user["type"] == "staff"

# Adds a new user to the database
def add_user(name, password, utype="user"):
    users = get_users()
    if users == None:
        users = []

    users.append({
        "id": str(uuid.uuid4()),
        "name": name,
        "password": password,
        "type": utype
    })

    db.set("users", users)
