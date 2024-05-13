# -------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files and
# exception handling
# Change Log:
#   aliciad, 05/13/2024, Created script
# -------------------------------------------------------------------------- #

from sys import exit

# Define the data constants
MENU: str = """
    ---- Course Registration Program ----
    Select from the following menu:
    1. Register a student for the course
    2. Show current data
    3. Save data to file
    4. Exit the program
    -------------------------------------
"""
FILE_NAME: str = "enrollments.csv"

# Define the data variables
file = None
student: str = ""
students: list[dict[str, str]] = []
menu_choice: str = ""
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: dict = {}
csv_data: str = ""

# Open enrollments.csv and loads data to lists at program launch
# Error handling included if file not found
try:    
    with open(FILE_NAME, "r") as file:
        file_data = file.readlines()
        for student in file_data:
            line = student.strip().split(",")
            row_dict = {
                "first_name": line[0],
                "last_name": line[1],
                "course_name": line[2]
            }
            students.append(row_dict)
    print("INFO: enrollments.csv file read into database.")
except FileNotFoundError:
    print("ERROR: Database file not found.")

# Present and process the data
while True:
    # Prints menu options to user
    print(MENU)
    menu_choice = input("Choose a menu option (1-4): ")
    # Prompts the user for the registration information
    if menu_choice == "1":
        # SError handling for non-alpha or empty strings
        try:
            student_first_name = input("Enter the student's first name: ")
            if len(student_first_name) == 0:
                raise ValueError("First name can't be empty.")
            if not student_first_name.isalpha():
                raise ValueError("First name can't contain non-alphanumeric values.")
            student_last_name = input("Enter the student's last name: ")
            if len(student_last_name) == 0:
                raise ValueError("Last name can't be empty.")
            if not student_last_name.isalpha():
                raise ValueError("Last name can't contain non-alphanumeric values.")
            course_name = input("Enter the course name: ")
            if len(course_name) == 0:
                raise ValueError("Course name can't be empty.")
            # Adds user input to dictionary
            student_data = {
                "first_name": student_first_name,
                "last_name": student_last_name,
                "course_name": course_name
            }
            students.append(student_data)
            # Prints confirmation that user's input has been accepted
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as error_details:
            print("-"*50)
            print(f"ERROR: {error_details}")
            print("**Technical Error Details**")
            print(error_details.__doc__)
    # Prints out all users input in a csv format
    elif menu_choice == "2":
        print("The current data is:")
        for student in students:
            print(f"{student["first_name"]}, {student["last_name"]}, {student["course_name"]}")
    # Adds user's input to csv file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                for student in students:
                    csv_data = f"{student["first_name"]}, {student["last_name"]}, {student["course_name"]}\n"
                    file.write(csv_data)
            print("INFO: New registrations have been saved to file.")
        except Exception as exception_details:
            print("-"*50)
            print(f" UNKNOWN ERROR: {exception_details}")
            print("---Technical Error Details---")
            print(exception_details.__doc__)
    # Exits the program
    elif menu_choice == "4":
        print("Program Ended")
        exit()
    # Displays a message if the user enters a value other than 1-4
    else:
        print("That's not a valid option.")
