import os

FILEPATH = 0

############################################

class Student:

    def __init__ (self, firstname, lastname, tnumber, score):
        
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = score

###########################################
#RUN_AV

    def RunningAverages(self):
        Scores = []
        for score in self.Grades:
            if score.strip():
                Scores.append(int(score))
        
        if not Scores:
            return 0
        
        return sum(Scores) / len(Scores)
    
#########################################
#SEM_AV

    def TotalAverage(self):
        total_sum = 0
        total_count = len(self.Grades)

        for score in self.Grades:
            if score.strip():
                total_sum += int(score)

        if total_count == 0:
            return 0
        
        return total_sum / total_count
    
##########################################
#GRADIN

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

########################################################

class StudentList: 
    
    def __init__ (self):
        self.Studentlist = []

#################################

    def add_student(self):
        newstudent = Student(firstname, lastname, tnumber)
        self.Studentlist.append(newstudent)

######################

    def find_student(self, tnumber: str) -> int:

        for index, student in enumerate(self,Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

###############################33

    def print_student_list(self):
        