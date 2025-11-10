import os

class Student:

    def __init__ (self, firstname, lastname, tnumber, score=None):
        
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = score if score is not None else [] 

#######################################

    def RunningAverages(self):
        Scores = []
        for score in self.Grades:
            if score.strip():
                Scores.append(int(score))
        
        if not Scores:
            return 0
        
        return sum(Scores) / len(Scores)
    
#######################################

    def TotalAverage(self):
        Scores = []
        for score in self.Grades:
            if score.strip():
                Scores.append(int(score))

        if not Scores:
            return 0
        
        return sum(Scores) / len(Scores) 
    
#######################################

    def LetterGrade(self):
        average = self.TotalAverage()

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
        
#######################################
