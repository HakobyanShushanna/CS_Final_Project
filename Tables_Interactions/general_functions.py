import bcrypt
import csv

#### PASSWORD ####
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def check_password(input_password, registered_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), registered_password)

#### BASIC FUNCTIONS ####
def search(email, data):
    for line in data:
        if line["Email"] == email:
            return line  
    return None

def remove(email, data):
    result = search(email, data)
    if result != None:
        data.remove(result)
        rewrite_data()

#### WORK WITH FILE ####
def get_data(file):
    with open(file, newline="") as admins:
        reader = csv.DictReader(admins)
        data = list(reader) 
        return data

def rewrite_data(file, data):
    with open(file, "w", newline="") as admins:
            fieldnames = data[0].keys() if data else []
            writer = csv.DictWriter(admins, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
