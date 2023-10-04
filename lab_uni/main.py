from general_func import GeneralOperations
from faculty_func import FacultyOperations
from student_func import StudentOperations
from student import Student


class University:
    def __init__(self):
        self.file_name_enrolled = "enrolled_students.txt"
        self.file_name_faculties = "faculties.txt"
        self.file_name_graduates = "graduated_students.txt"
        self.file_name_congratulation_enrolling = "message_enroll.txt"
        self.file_name_congratulation_graduating = "message_graduate.txt"
        self.general_manager = GeneralOperations(self.file_name_faculties, self.file_name_enrolled)
        self.faculty_manager = FacultyOperations(self.file_name_faculties, self.file_name_enrolled,
                                                 self.file_name_graduates, self.file_name_congratulation_enrolling,
                                                 self.file_name_congratulation_graduating)
        self.student_manager = StudentOperations(self.file_name_enrolled, self.file_name_faculties,
                                                 self.file_name_congratulation_enrolling)

    def run(self):
        print("Welcome to University's student manager system!\n")

        while True:
            current_datetime = input("Enter current date (yyyy/mm/dd): ")
            try:
                Student.correct_format_date(current_datetime)
                break
            except ValueError as e:
                print(e)

        print("What do you want to do?\n")

        while True:
            print("g - General operations")
            print("f - Faculty operations")
            print("s - Student operations")
            print("\nq - Quit the program")
            choice = input("Enter your choice: ")

            if choice == "g":
                menu_options_general = {
                    1: self.general_manager.input_faculty,
                    2: self.general_manager.search_student_what_faculty,
                    3: self.general_manager.display_faculties,
                    4: self.general_manager.display_faculties_by_field,
                    5: lambda: print("Going back to the previous menu."),
                    6: lambda: (print("Exiting the program.") or exit())
                }

                while True:
                    print("General operations\n")
                    print("What do you want to do?")
                    print("1 - Create a faculty")
                    print("2 - Search what faculty students belong to")
                    print("3 - Display university faculties")
                    print("4 - Display all faculties belonging to a field")
                    print("5 - Back")
                    print("6 - Quit the program\n")

                    try:
                        choice_general = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric choice.")
                        continue

                    if choice_general in menu_options_general:
                        menu_options_general[choice_general]()  # Execute the corresponding method
                        if choice_general in {5, 6}:
                            break
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "f":
                menu_options_faculty = {
                    1: self.faculty_manager.assign_student_to_faculty,
                    2: self.faculty_manager.add_student,
                    3: self.faculty_manager.graduate_student,
                    4: self.faculty_manager.display_enrolled_students,
                    5: self.faculty_manager.display_graduated_students,
                    6: lambda: print("Going back to the previous menu."),
                    7: lambda: (print("Exiting the program.") or exit())
                }

                while True:
                    print("Faculty operations\n")
                    print("What do you want to do?")
                    print("1 - Assign student to a faculty")
                    print("2 - Create a student and directly assign to a faculty")
                    print("3 - Graduate a student from a faculty")
                    print("4 - Display current enrolled students")
                    print("5 - Display graduates")
                    print("6 - Back")
                    print("7 - Quit the program\n")

                    try:
                        choice_faculty = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric choice.")
                        continue

                    if choice_faculty in menu_options_faculty:
                        menu_options_faculty[choice_faculty]()  # Execute the corresponding method
                        if choice_faculty in {6, 7}:
                            break
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "s":
                menu_options_student = {
                    1: self.student_manager.input_student,
                    2: self.student_manager.delete_student_by_email,
                    3: lambda: print("Going back to the previous menu."),
                    4: lambda: (print("Exiting the program.") or exit())
                }

                while True:
                    print("Student operations\n")
                    print("What do you want to do?")
                    print("1 - Enroll student to university")
                    print("2 - Kick student from university")
                    print("3 - Back")
                    print("4 - Quit the program\n")

                    try:
                        choice_student = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric choice.")
                        continue

                    if choice_student in menu_options_student:
                        menu_options_student[choice_student]()  # Execute the corresponding method
                        if choice_student in {3, 4}:
                            break
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == "q":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    uni = University()
    uni.run()
