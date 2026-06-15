"""Class objects for the DB"""

from datetime import datetime

class User(dict):
    """Creates the user with the unique UUID and current date"""
    def __init__(self,UUID:str,name:str,password:str,admin=False):
        super().__init__()
        self["_id"] = UUID
        self["name"] = name 
        self["password"] = password 
        self["admin"] = admin 
        self["creation"] = datetime.now().strftime("%d-%m-%y") 

class Training(dict):
    """Contains Eyegaze json and time+date of the training with feedback received"""
    def __init__(self,UUID:str,eye: dict,feedback:str):
        super().__init__()
        self["UUID"] = UUID
        self["feedback"] = feedback
        self["eye"] = eye
        self["date"] = datetime.now().strftime("%H:%M/%d-%m-%y") 

class Progress:
    """Contains the UUID and a list of all the trainings the user has had"""
    def __init__(self,UUID:str,trainings:list[Training]):
        self.UUID = UUID
        self.trainings = trainings
    def append_trainign(self,training:Training):
        self.trainings.append(training)
    def return_trainings(self):
        return self.trainings

        