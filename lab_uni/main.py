from general_func import GeneralOperations
from faculty_func import FacultyOperations
from student_func import StudentOperations
from student import Student

class University:
    def __init__(self):
        self.file_name_enrolled = "current_enrolled_students.txt"
        self.file_name_faculties = "faculties.txt"
        self.file_name_graduates = "graduated_students.txt"
        self.file_name_congratulation_enrolling = "congratulation_enrolling.txt"
        self.file_name_congratulation_graduating = "congratulation_graduating.txt"
        self.general_manager = GeneralOperations(self.file_name_faculties, self.file_name_enrolled)
        self.faculty_manager = FacultyOperations(self.file_name_faculties, self.file_name_enrolled,
                                                 self.file_name_graduates, self.file_name_congratulation_enrolling,
                                                 self.file_name_congratulation_graduating)
        self.student_manager = StudentOperations(self.file_name_enrolled, self.file_name_faculties,
                                                 self.file_name_congratulation_enrolling)

    def run(self):
        print("Welcome to University's manager system!\n")
        while True:
            current_datetime = input("Enter current date (yyyy/mm/dd): ")
            try:
                Student.validate_date(current_datetime)
                break
            except ValueError as e:
                print(e)
        
        while True:
            print("What do you want to do?\n")
            print("g - General operations")
            print("f - Faculty operations")
            print("s - Student operations")
            print("q - Quit the program")
            choice = input("Enter your choice: ")

            if choice == "g":
                self.general_operations(current_datetime)
            elif choice == "f":
                self.faculty_operations(current_datetime)
            elif choice == "s":
                self.student_operations(current_datetime)
            elif choice == "q":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def general_operations(self, current_datetime):
        while True:
            print("\nGeneral operations\n")
            print("1 - Create a faculty")
            print("2 - Search what faculty students belong to")
            print("3 - Display university faculties")
            print("4 - Display all faculties belonging to a field")
            print("5 - Back")
            print("6 - Quit the program\n")

            choice_g = input("Enter your choice: ")

            if choice_g == "1":
                self.general_manager.input_faculty()
            elif choice_g == "2":
                self.general_manager.search_student_what_faculty()
            elif choice_g == "3":
                self.general_manager.display_faculties()
            elif choice_g == "4":
                self.general_manager.display_faculties_by_field()
            elif choice_g == "5":
                break
            elif choice_g == "6":
                print("Exiting the program.")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def faculty_operations(self, current_datetime):
        while True:
            print("\nFaculty operations\n")
            print("1 - Assign student to a faculty")
            print("2 - Create a student and directly assign to a faculty")
            print("3 - Graduate a student from a faculty")
            print("4 - Display current enrolled students")
            print("5 - Display graduates")
            print("6 - Back")
            print("7 - Quit the program\n")

            choice_f = input("Enter your choice: ")

            if choice_f == "1":
                self.faculty_manager.assign_student_to_faculty()
            elif choice_f == "2":
                self.faculty_manager.input_and_assign_student()
            elif choice_f == "3":
                self.faculty_manager.graduate_student()
            elif choice_f == "4":
                self.faculty_manager.display_enrolled_students()
            elif choice_f == "5":
                self.faculty_manager.display_graduated_students()
            elif choice_f == "6":
                break
            elif choice_f == "7":
                print("Exiting the program.")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def student_operations(self, current_datetime):
        while True:
            print("\nStudent operations\n")
            print("1 - Enroll student to university")
            print("2 - Kick student from university")
            print("3 - Back")
            print("4 - Quit the program\n")

            choice_s = input("Enter your choice: ")

            if choice_s == "1":
                self.student_manager.input_student()
            elif choice_s == "2":
                self.student_manager.delete_student_by_email()
            elif choice_s == "3":
                break
            elif choice_s == "4":
                print("Exiting the program.")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

  

if __name__ == "__main__":
    uni = University()
    uni.run()
