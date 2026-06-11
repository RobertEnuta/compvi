# CRUD FOR DB
import pymongo
from db import DBC as conn

DB_NAME="database"

def check_client():
    client = conn.connect_db() 
    if client is not None:
        return client

def create_db(name=DB_NAME):
    client = check_client() 
    if client is not None:
        db = client[name]
        print(f"Created {name}")
        return db

def check_db(name=DB_NAME):
    client = check_client()
    if client is not None:
        dblist = client.list_database_names()
        if name in dblist:
            # print(f"{name} exists.")   
            return client[name]
    else: print("No connection")

def del_db(name=DB_NAME):
    client = conn.connect_db() 
    if client is not None:
        client.drop_database(name)
        print(f"Deleted {name}")
        return