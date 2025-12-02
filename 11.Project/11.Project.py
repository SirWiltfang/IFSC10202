import os

class Student:

    def __init__ (self, firstname, lastname, tnumber, score=None):
        
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = score if score is not None else [] 
        self.TotalAssignments = 0 

#######################################

    def RunningAverages(self):
        Scores = []
        for score in self.Grades:
            if score.strip():
                Scores.append(int(score))
        
        if not Scores:
            return 0.0
        
        return sum(Scores) / len(Scores)
    
#######################################

    def TotalAverage(self):
        num_assignments = self.TotalAssignments
        
        if num_assignments == 0:
            return 0.0

        total_score = 0
        for score in self.Grades:
            if score.strip():
                total_score += int(score)

        return total_score / num_assignments 
    
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
        
####################################################3####3
#Second MAin
class StudentList: 
    
    def __init__ (self):
        self.Studentlist = []
        self.MaxAssignments = 0 

#######################################

    def add_student(self, firstname, lastname, tnumber, score=None):
        
        newstudent = Student(firstname, lastname, tnumber, score) 
        self.Studentlist.append(newstudent)

#######################################

    def find_student(self, tnumber):

        for index, student in enumerate(self.Studentlist): 
            if student.TNumber == tnumber:
                return index
        return -1

#######################################

    def print_student_list(self):

        HEADER = (
            f"\n{'First':>12}{'Last':>12}{'ID':>12}{'Running':>12}{'Semester':>12}{'Letter':>12}\n"
            f"{'Name':>12}{'Name':>12}{'Number':>12}{'Average':>12}{'Average':>12}{'Grade':>12}\n"
            f"{'-'*12}{' '}{'-'*11}{' '}{'-'*11}{' '}{'-'*11}{' '}{'-'*11}{' '}{'-'*11}" 
        )
        print(HEADER)

        for student in self.Studentlist:
            student.TotalAssignments = self.MaxAssignments

        for student in self.Studentlist:
            running_avg = student.RunningAverages() 
            total_avg = student.TotalAverage()
            letter_grade = student.LetterGrade()

            output = (
                        f"{student.FirstName:>12}"
                        f"{student.LastName:>12}"
                        f"{student.TNumber:>12}"
                        f"{running_avg:>12.2f}"
                        f"{total_avg:>12.2f}"
                        f"{letter_grade:>12}"
                        )
            print(output)

#######################################

    def add_student_from_file(self, filename):
        with open(filename, 'r') as openfile:
            for line in openfile:
                if not line.strip():
                    continue

                parts = line.strip().split(',')

                if len(parts) >= 3:
                    first_name, last_name, t_number = [p.strip() for p in parts[:3]]
                    self.add_student(first_name, last_name, t_number, []) 

#######################################
    
    def add_scores_from_file(self, filename):
        temp_scores_tracker = {student.TNumber: [] for student in self.Studentlist}
        
        with open(filename, 'r') as openfile:
            for line in openfile:
                if not line.strip():
                    continue

                parts = line.strip().split(',')
                
                if len(parts) >= 2: 
                    t_number = parts[0].strip() 
                    score = parts[1].strip()

                    if t_number in temp_scores_tracker:
                        temp_scores_tracker[t_number].append(score)

        if not temp_scores_tracker:
            return

        self.MaxAssignments = max(len(scores) for scores in temp_scores_tracker.values())
        
        for student in self.Studentlist:
            t_number = student.TNumber
            if t_number in temp_scores_tracker:
                student.Grades = temp_scores_tracker[t_number]
            
            student.TotalAssignments = self.MaxAssignments

#######################################1

STUDENTFILE = "11.Project/11.Project Students.txt"
SCOREFILE = "11.Project/11.Project Scores.txt"

def main():

    student_list_manager = StudentList()
    student_list_manager.add_student_from_file(STUDENTFILE)
    student_list_manager.add_scores_from_file(SCOREFILE)
    student_list_manager.print_student_list()

if __name__ == "__main__":
    main()
    