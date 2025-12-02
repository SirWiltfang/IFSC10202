

import os


class Employee:
    
    def __init__(self, emp_num, first_name, last_name, address, city, state, zip_code):
        
        self.EmployeeNumber = emp_num
        self.FirstName = first_name
        self.LastName = last_name
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zip_code


class EmployeeList:
    
    
    def __init__(self, filename):
        
        self.EmployeeList = []
        self.filename = filename
        self.ReadEmployeeFile()

####################################################

    def ReadEmployeeFile(self):
        
        if not os.path.exists(self.filename):
            print(f"File '{self.filename}' not found. Starting with an empty employee list.")
            return

        try:
            with open(self.filename, 'r') as openfile:
                for line in openfile:
                    if not line.strip():
                        continue
                    
                    parts = [p.strip() for p in line.strip().split(',')]
                    
                    if len(parts) == 7:
                        
                        try:
                            emp_num = int(parts[0])
                        except ValueError:
                            
                            continue 
                            
                        
                        new_employee = Employee(emp_num, parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
                        self.EmployeeList.append(new_employee)
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

####################################################

    def WriteEmployeeFile(self):
        
        try:
            directory = os.path.dirname(self.filename)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            with open(self.filename, 'w') as outfile:
                for employee in self.EmployeeList:
                    
                    line = f"{employee.EmployeeNumber},{employee.FirstName},{employee.LastName},{employee.Address},{employee.City},{employee.State},{employee.Zip}\n"
                    outfile.write(line)
            print("Changes saved to file successfully.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

####################################################

    def DisplayEmployeeList(self):
        
        if not self.EmployeeList:
            print("\nNo employees to display.")
            return
        
        HEADER = (
            f"\n{'Employee':<15}{'First':<15}{'Last':<15}{'Address':<20}{'City':<15}{'State':<10}{'Zip':<10}\n"
            f"{'Number':<15}{'Name':<15}{'Name':<15}\n"
            f"{'-'*15}{'-'*15}{'-'*15}{'-'*20}{'-'*15}{'-'*10}{'-'*10}"
        )
        print(HEADER)
        
        for employee in self.EmployeeList:
            output = (
                f"{employee.EmployeeNumber:<15}"
                f"{employee.FirstName:<15}"
                f"{employee.LastName:<15}"
                f"{employee.Address:<20}"
                f"{employee.City:<15}"
                f"{employee.State:<10}"
                f"{employee.Zip:<10}"
            )
            print(output)
        print()

####################################################

    def ReadEmployee(self, employee_number):
        
        index = self.FindEmployee(employee_number)
        if index != -1:
            employee = self.EmployeeList[index]
            return (
                employee.EmployeeNumber, employee.FirstName, employee.LastName, 
                employee.Address, employee.City, employee.State, employee.Zip
            )
        return None
    
####################################################

    def NextEmployeeNumber(self):
        
        if not self.EmployeeList:
            return 1
        
        
        sorted_employees = sorted(self.EmployeeList, key=lambda emp: emp.EmployeeNumber)
        last_number = sorted_employees[-1].EmployeeNumber
        return last_number + 1
    
####################################################

    def AddEmployee(self, first_name, last_name, address, city, state, zip_code):
        
        new_emp_num = self.NextEmployeeNumber()
        
        
        new_employee = Employee(
            new_emp_num, first_name, last_name, address, city, state, zip_code
        )
        
        self.EmployeeList.append(new_employee)

####################################################

    def UpdateEmployee(self, employee_number, first_name, last_name, address, city, state, zip_code):
        
        index = self.FindEmployee(employee_number)
        
        if index != -1:
            employee = self.EmployeeList[index]
            employee.FirstName = first_name
            employee.LastName = last_name
            employee.Address = address
            employee.City = city
            employee.State = state
            employee.Zip = zip_code
            return True
        return False
    
#####################################################

    def DeleteEmployee(self, employee_number):
        
        index = self.FindEmployee(employee_number)
        
        if index != -1:
            del self.EmployeeList[index]
            return True
        return False
    
####################################################

    def FindEmployee(self, employee_number):
        
        for index, employee in enumerate(self.EmployeeList):
            if employee.EmployeeNumber == employee_number:
                return index
        return -1
    
##########################

def get_input(prompt, required=True):
    
    while True:
        value = input(prompt).strip()
        if required and not value:
            print("This field is required. Please enter a value.")
            continue
        return value
    
###################################

def validate_state(prompt):
    
    while True:
        state = input(prompt).strip()
        
        if len(state) == 2 and state.isalpha() and state.isupper():
            return state
        print("Invalid state. State must be exactly two capitalized letters (e.g., AR).")

########################################

def validate_zip(prompt):
    
    while True:
        zip_code = input(prompt).strip()
        if zip_code.isdigit() and len(zip_code) == 5:
            return zip_code
        print("Invalid Zip code. Must be 5 numeric digits.")

##############################

def validate_emp_num(prompt):
    
    while True:
        emp_num_str = input(prompt).strip()
        try:
            return int(emp_num_str)
        except ValueError:
            print("Invalid input. Employee Number must be an integer.")

##########################

def add_new_employee(employee_list):
    
    print("\n--- Add a New Employee ---")
    
    
    first_name = get_input("Enter First Name: ")
    last_name = get_input("Enter Last Name: ")
    address = get_input("Enter Address: ")
    city = get_input("Enter City: ")
    state = validate_state("Enter State (e.g., AR): ")
    zip_code = validate_zip("Enter Zip: ")
    
    employee_list.AddEmployee(first_name, last_name, address, city, state, zip_code)
    print("Employee Added")

############################

def delete_existing_employee(employee_list):
    
    print("\n--- Delete an Existing Employee ---")
    
    emp_num = validate_emp_num("Enter Employee Number to delete: ")
    
    if employee_list.DeleteEmployee(emp_num):
        print("Employee Deleted")
    else:
        print(f"Error: Employee Number {emp_num} does not exist.")

#########################################

def change_existing_employee(employee_list):
    
    print("\n--- Change an Existing Employee ---")
    
    emp_num = validate_emp_num("Enter Employee Number to change: ")
    
    employee_index = employee_list.FindEmployee(emp_num)
    if employee_index == -1:
        print(f"Error: Employee Number {emp_num} not found.")
        return

    
    employee = employee_list.EmployeeList[employee_index]
    
    while True:
        print("\n(F)irst Name(L)Last Name(A)ddress(C)ity(S)tate(Z)Zip(B)ack to Main Menu")
        sub_selection = input("Enter Selection: ").strip().upper()

        if sub_selection == 'B':
            break

        current_data = {
            'F': employee.FirstName,
            'L': employee.LastName,
            'A': employee.Address,
            'C': employee.City,
            'S': employee.State,
            'Z': employee.Zip
        }
        
        if sub_selection in current_data:
            field_name = {
                'F': 'First Name', 'L': 'Last Name', 'A': 'Address', 
                'C': 'City', 'S': 'State', 'Z': 'Zip'
            }[sub_selection]
            
            print(f"Current {field_name}: {current_data[sub_selection]}")
            
            
            if sub_selection == 'F':
                employee.FirstName = get_input(f"Enter New {field_name}: ")
            elif sub_selection == 'L':
                employee.LastName = get_input(f"Enter New {field_name}: ")
            elif sub_selection == 'A':
                employee.Address = get_input(f"Enter New {field_name}: ")
            elif sub_selection == 'C':
                employee.City = get_input(f"Enter New {field_name}: ")
            elif sub_selection == 'S':
                employee.State = validate_state(f"Enter New {field_name} (e.g., AR): ")
            elif sub_selection == 'Z':
                employee.Zip = validate_zip(f"Enter New {field_name}: ")
            
            print(f"{field_name} updated successfully.")
            
        else:
            print("Invalid selection. Please try again.")

#####################################

EMPLOYEE_FILE = "Final/Final Project Employees.txt"



def main():
    
    
    employee_list_manager = EmployeeList(EMPLOYEE_FILE)
    
    while True:
        
        print("(A)dd a New Employee(D)elete an Existing Employee(C)hange an Existing Employee(P)rint All Employees(S)ave Changes to File(Q)uit")
        selection = input("Enter Selection: ").strip().upper()
        
        if selection == 'A':
            add_new_employee(employee_list_manager)
        elif selection == 'D':
            delete_existing_employee(employee_list_manager)
        elif selection == 'C':
            change_existing_employee(employee_list_manager)
        elif selection == 'P':
            employee_list_manager.DisplayEmployeeList()
        elif selection == 'S':
            employee_list_manager.WriteEmployeeFile()
        elif selection == 'Q':
            print("Good-bye")
            break
        else:
            print("Invalid selection. Please enter A, D, C, P, S, or Q.")

if __name__ == "__main__":
    main()




