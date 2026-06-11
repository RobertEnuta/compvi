import json
import colCRUD as col
import dbCRUD as db
import Class as dbc

DEFAULT_USERNAME = "000000DEFAULTUSERNAME000000"

def create_user(UUID:str,name=DEFAULT_USERNAME):
    u = dbc.User(UUID,name)
    return u

def create_training(eye:dict,feedback:str):
    t = dbc.Training(eye,feedback)
    return t
    
def create_prog(userUUID:str,trainings:list[dict]):
    prog = dbc.Progress(userUUID,trainings)
    return prog

def add_prog(prog:dbc.Progress,training:dbc.Training):
    prog.append_trainign(training)
    print("Progress has been added")
    return 

if __name__== '__main__':
    with open(".\\collected\\token.txt", "r") as f:
        UUID = f.read()
    requesting =[]
    with open(".\\collected\\feedback.json", "r") as fb:
        for jsonObj in fb:
            myDict = json.loads(jsonObj)
            # requesting.append(InsertOne(myDict))
            print(myDict)
        
    # dummy1 = create_user(UUID)
    # print(dummy1)
    # print(dummy1.UUID)
    # print(dummy1.name)
    # print(dummy1.creation)


