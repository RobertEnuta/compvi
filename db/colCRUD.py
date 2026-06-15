from typing import Collection
import dbCRUD as DB

DB_NAME="database"

def create_col(name,dbName=DB_NAME):
    db = DB.check_db(dbName)
    if db is not None:
        col = db[name]
        return col
    else:
        db = DB.create_db(dbName)
        col = db[name]
        return col


def read_col(col: Collection,query={}):
    if col is not None:
        data =[]
        for x in col.find(query):
            data.append(x)
        return data

def clear_col(col: Collection):
    if col is not None:
        col.delete_many({})


