import os

FILEPATH = "10.Project/10.Project Student Scores.txt"

class Student:

    def __init__(self, firstname, lastname, tnumber, score):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = score

    def RunningAverages(self):
        Scores = [int(score) for score in self.Grades if score.strip()]
        return sum(Scores) / len(Scores) if Scores else 0

    def TotalAverage(self):
        Scores = [int(score) for score in self.Grades if score.strip()]
        return sum(Scores) / len(self.Grades) if self.Grades else 0

    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90: return "A"
        elif average >= 80: return "B"
        elif average >= 70: return "C"
        elif average >= 60: return "D"
        else: return "F"

def Student_scores(filepath):
    HEADER = (
        f"\n{'First':>12}{'Last':>12}{'ID':>12}{'Running':>12}{'Semester':>12}{'Letter':>12}\n"
        f"{'Name':>12}{'Name':>12}{'Number':>12}{'Average':>12}{'Average':>12}{'Grade':>12}\n"
        f"{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}"
    )

    print(HEADER)

    with open(filepath, 'r') as file:
        for line in file:
            parts = [p.strip() for p in line.strip().split(',')]

            if len(parts) < 4:
                continue

            student = Student(parts[0], parts[1], parts[2], parts[3:])

            running_average = student.RunningAverages()
            total_average = student.TotalAverage()
            let_grade = student.LetterGrade()

            output = (
                f"{student.FirstName:>12}"
                f"{student.LastName:>12}"
                f"{student.TNumber:>12}"
                f"{running_average:>12.2f}"
                f"{total_average:>12.2f}"
                f"{let_grade:>12}"
            )

            print(output)
    print("\n")

if __name__ == "__main__":
    Student_scores(FILEPATH)