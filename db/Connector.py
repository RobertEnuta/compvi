from db import colCRUD as col
from db import Class as dbc
import pymongo
DEFAULT_USERNAME = "000000DEFAULTUSERNAME000000"
ProgDB = "ProgDB"
def create_user(UUID:str,name=DEFAULT_USERNAME):
    """Create a new user and upload to the db"""
    u = dbc.User(UUID,name)
    c = col.create_col("users","userDB")
    try:
        c.insert_one(u)
        print("User added successfully!")
    except pymongo.errors.DuplicateKeyError:
        print("User already exists!")
    return u

def create_training(UUID:str,eye:dict,feedback:str):
    """Create a training object and upload it the the DB"""
    t = dbc.Training(UUID,eye,feedback)
    try:
        c = col.create_col("progress",ProgDB)
        c.insert_one(t)
        print("Training saved successfully!")
    except:
        print("Something went wrong!")
    return t

def read_users(query={}):
    """query must be a dict object {"name":"test"} or be left empty to select all users"""
    users =[]
    c = col.create_col("users","userDB")
    for u in c.find(query):
        users.append(u)
    return users

def read_prog(query={}):
    """query must be a dict object {"date":"10:15/11-06-26"} or be left empty to select all users"""
    prog =[]
    c = col.create_col("progress",ProgDB)
    for t in c.find(query):
        prog.append(t)
    return prog
