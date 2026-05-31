from typing import Collection
import dbCRUD as DB
import dbConnection as con

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


def read_col(col: Collection,query):
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
    print(client.list_database_names())
    col = create_col("clients","users")
    clear_col(col)
    query = {"address":"Mountain 21"}
    mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Mountain 21"},
  { "name": "Ben", "address": "Mountain 21"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}]
    insert_col(col,mylist)
    print(read_col(col,query))