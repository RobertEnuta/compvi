"""Import script to connect to mongodb instance"""

import pymongo
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 


def connect_db():
    # accessing and printing value
    url = os.getenv("DB_URL")
    myclient = pymongo.MongoClient(url)
    myclient._connect()
    return myclient




