import colCRUD as col
import Class as dbc
import pymongo
DEFAULT_USERNAME = "000000DEFAULTUSERNAME000000"
ProgDB = "ProgDB"
def create_user(UUID:str,password:str,name=DEFAULT_USERNAME):
    """Create a new user and upload to the db"""
    u = dbc.User(UUID,name,password)
    c = col.create_col("users","userDB")
    try:
        c.insert_one(u)
        return(f"User:{name} added successfully!")
    except pymongo.errors.DuplicateKeyError:
        return(f"User:{name} already exists!")

def update_user(query:dict,token:str):
    """Update token in the db"""
    c = col.create_col("users","userDB")
    try:
        c.update_one(query,{"$set": {"token": token}})
        return "Token updated"
    except:
        return "User could not be updated" 

def del_user(name:str,password:str):
    """Update token in the db"""
    c = col.create_col("users","userDB")
    try:
        c.delete_one({"name":name,"password":password})
        return f"{name} deleted"
    except:
        return f"User {name} could not be deleted" 

def login_user(UUID:str,password:str,name:str):
    """Check user exists"""
    u = dbc.User(UUID,name,password)
    c = col.create_col("users","userDB")
    try:
        c.find_one(u)
        return True
    except:
        return False


def create_training(UUID:str,eye:dict,feedback:str):
    """Create a training object and upload it the the DB"""
    t = dbc.Training(UUID,eye,feedback)
    try:
        c = col.create_col("progress",ProgDB)
        c.insert_one(t)
        return(f"Training for {UUID} saved successfully!")
    except:
        return("Something went wrong!")


def read_users(query={}) ->  list[dbc.User]:
    """query must be a dict object {"name":"test"} or be left empty to select all users"""
    users =[]
    c = col.create_col("users","userDB")
    for u in c.find(query):
        users.append(u)
    return users

def read_prog(UUID:str):
    """query must be a dict object {"date":"10:15/11-06-26"} or be left empty to select all users"""
    prog =[]
    c = col.create_col("progress",ProgDB)
    for t in c.find({"UUID":UUID}):
        prog.append(t)
    return prog

def del_prog(UUID):
    c = col.create_col("progress",ProgDB)
    for t in c.find({"UUID":UUID}):
        c.delete_many()
    return f"Progress has been deleted for {UUID}"
