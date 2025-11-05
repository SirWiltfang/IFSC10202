
import math
import os

FILEPATH = "10.Project/10.Project Student Scores.txt"

############################################

class Student:

    def __init__ (self, firstname, lastname, tnumber, score):
        
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = score


    def runningaverage(self):
        Scores = []
        

##########################################
#GRADIN

    def L_grading(self):

        average = self.total_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
            
################################################


