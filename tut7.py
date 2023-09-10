from datetime import datetime

class Student:
    def __init__(self,name,dob,branch,credits):
        self.name=name
        self.dob=dob
        self.branch=branch
        self.credits=credits


    def get_age(self):
        # print((datetime.now()-self.dob).days//365)
        return (datetime.now()-self.dob).days//365
    
    def get_credits(self):
        return self.credits
    

def get_topper(listOfMarks):
    print(   max(listOfMarks,key=lambda student :student.get_credits()))
    return max(listOfMarks,key=lambda student :student.get_credits())