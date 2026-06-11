"""Class objects for the DB"""

from datetime import datetime


class User:
    """Creates the user with the unique UUID and current date"""
    def __init__(self,UUID:str,name:str):
        self.UUID = UUID
        self.name = name 
        self.creation = datetime.now().strftime("%d-%m-%y") 

class Training:
    """Contains Eyegaze json and time+date of the training with feedback received"""
    def __init__(self,eye: dict,feedback:str):
        self.feedback = feedback
        self.eye = eye
        self.date = datetime.now().strftime("%H:%M/%d-%m-%y") 

class Progress:
    """Contains the UUID and a list of all the trainings the user has had"""
    def __init__(self,UUID:str,trainings:list[Training]):
        self.UUID= UUID
        self.trainings = trainings
    def append_trainign(self,training:Training):
        self.trainings.append(training)
    def return_trainings(self):
        return self.trainings

        