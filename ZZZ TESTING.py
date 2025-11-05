import os

# Define the file path as requested
FILE_PATH = "10.Project/10.Project Student Scores.txt"

# --- Step 1, 2, 3: Create the Student class and its initializer ---
class Student:
    """
    A class to represent a student and calculate their various grade averages and letter grade.
    """
    def __init__(self, firstname, lastname, tnumber, scores):
        """
        Initializes a new Student object.
        :param firstname: Student's first name (string)
        :param lastname: Student's last name (string)
        :param tnumber: Student's ID number (string)
        :param scores: A list of string scores, variable in length (List[str])
        """
        # Step 3: Create object attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber.strip()  # Clean up T-number just in case
        self.Grades = scores

    # --- Step 4: Define the methods for the object ---

    def RunningAverage(self):
        """
        Calculates the running average (non-blank scores only).
        :return: The running average (float)
        """
        valid_scores = []
        for score in self.Grades:
            # Check if the score string is not empty
            if score.strip():
                try:
                    # Convert to integer and add to the list
                    valid_scores.append(int(score))
                except ValueError:
                    # Handle cases where a non-empty string isn't a valid number
                    continue

        if not valid_scores:
            return 0.0

        # Calculate the average of the valid scores
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):
        """
        Calculates the semester average, treating missing scores as zero.
        The divisor is the total number of grade slots (length of self.Grades).
        :return: The total/semester average (float)
        """
        total_score_sum = 0
        total_score_count = len(self.Grades)

        for score in self.Grades:
            # If the score is missing/blank, it's treated as 0, so we do nothing.
            if score.strip():
                try:
                    total_score_sum += int(score)
                except ValueError:
                    # Treat non-numeric non-blank scores as 0 for sum if necessary,
                    # but the problem implies they are blanks or valid numbers.
                    pass

        if total_score_count == 0:
            return 0.0

        # The total number of slots is the divisor (Joe Smith has 4, Jim Evans has 3, Jane Doe has 3)
        return total_score_sum / total_score_count

    def LetterGrade(self):
        """
        Returns the letter grade based on the TotalAverage.
        """
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

# --- Utility to create the file if it doesn't exist ---
def setup_file(filepath):
    """
    Creates the required data file for the program to run.
    """
    # Ensure the directory exists
    dir_name = os.path.dirname(filepath)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    # Content to be written to the file
    content = [
        "Jim,Evans,T123456,95,,71",
        "Joe,Smith,T654321,90,80,85,97",
        "Jane,Doe,T121212,,100,99"
    ]
    
    # Write the content to the file
    with open(filepath, 'w') as f:
        f.write('\n'.join(content))
    print(f"Data file created successfully at: {filepath}")

# --- Main Program Logic ---
def process_student_scores(filepath):
    """
    Reads the student score data, processes it using the Student class,
    and prints the formatted results.
    """
    # 1. Setup the header for the output
    header = (
        f"{'First':>12}{'Last':>12}{'ID':>12}{'Running':>12}{'Semester':>12}{'Letter':>12}\n"
        f"{'Name':>12}{'Name':>12}{'Number':>12}{'Average':>12}{'Average':>12}{'Grade':>12}\n"
        f"{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}{'-'*12}"
    )
    print(header)
    
    try:
        # Open and read the file
        with open(filepath, 'r') as f:
            # Use a single student object instance, reusing it for each line
            current_student = Student("", "", "", []) 
            
            for line in f:
                # Remove leading/trailing whitespace and split by comma
                parts = [p.strip() for p in line.strip().split(',')]
                
                # Basic check to ensure we have at least First, Last, T#, and one score
                if len(parts) < 4:
                    continue 

                # Extract the components
                first_name = parts[0]
                last_name = parts[1]
                t_number = parts[2]
                scores = parts[3:] # Everything after the T-number is a score

                # Re-initialize the object attributes for the current student
                current_student.FirstName = first_name
                current_student.LastName = last_name
                current_student.TNumber = t_number
                current_student.Grades = scores

                # Calculate the metrics
                running_avg = current_student.RunningAverage()
                total_avg = current_student.TotalAverage()
                letter_grade = current_student.LetterGrade()

                # Format and print the output line
                output_line = (
                    f"{current_student.FirstName:>12}"
                    f"{current_student.LastName:>12}"
                    f"{current_student.TNumber:>12}"
                    f"{running_avg:>12.2f}"  # Format to two decimal places
                    f"{total_avg:>12.2f}"    # Format to two decimal places
                    f"{letter_grade:>12}"
                )
                print(output_line)

    except FileNotFoundError:
        print(f"\nERROR: File not found at {filepath}. Please ensure the file is created.")

# --- Execution ---
if __name__ == "__main__":
    # Create the data file if it doesn't exist to ensure the script runs smoothly
    setup_file(FILE_PATH)
    
    # Process the data

    process_student_scores(FILE_PATH)