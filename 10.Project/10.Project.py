
import os

FILEPATH = "10.Project/10.Project Student Scores.txt"

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
            
################################################
#MAIN

def Student_scores(filepath):
    
#####################
#HEAD

    HEADER = (
        f"\n{'First':>12}{'Last':>12}{'ID':>12}{'Running':>12}{'Semester':>12}{'Letter':>12}\n"
        f"{'Name':>12}{'Name':>12}{'Number':>12}{'Average':>12}{'Average':>12}{'Grade':>12}\n"
        f"{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}"
    )

    print(HEADER)
    

###############################
#openfiel

    with open(filepath, 'r') as file:
        for line in file:
            clean_line = line.strip()
            parts = [p.strip() for p in clean_line.split(',')]
            
            if len(parts) < 4:
                continue
            first_name = parts[0]
            last_name = parts[1]
            t_number = parts[2]
            scores = parts[3:]

            currnet_student = Student(first_name, last_name, t_number, scores)

            running_average = currnet_student.RunningAverages()
            total_average = currnet_student.TotalAverage()
            let_grade = currnet_student.LetterGrade()

###################################

            output = (
                    f"{currnet_student.FirstName:>12}"
                    f"{currnet_student.LastName:>12}"
                    f"{currnet_student.TNumber:>12}"
                    f"{running_average:>12.2f}"
                    f"{total_average:>12.2f}"
                    f"{let_grade:>12}"
                )
            
            print(output)
    print("\n")

if __name__ == "__main__":
    Student_scores(FILEPATH)

