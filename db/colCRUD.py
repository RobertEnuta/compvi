from typing import Collection
import dbCRUD as DB
import DBC as con

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


def read_col(col: Collection,query: dict):
    if col is not None:
        data =[]
        for x in col.find(query):
            data.append(x)
        return data

def insert_col(col: Collection,data: dict | list[dict]):
    if col is not None:
        if type(data) == dict:
            col.insert_one(data)
        else:
            col.insert_many(data)
    return

def clear_col(col: Collection):
    if col is not None:
        col.delete_many({})


if __name__== '__main__':
    client = con.connect_db() 
    users = create_col("users","userDB")
    

    
    print(client.list_database_names())
    

