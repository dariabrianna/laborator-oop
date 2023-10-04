from student impor Student
from faculty_func import FacultyOperations

class StudentOperations:
    def __init__(self, file_name_enrolled, file_name_faculties, file_name_congratulation_enrolling):
        self.file_name_enrolled = file_name_enrolled
        self.file_name_faculties = file_name_faculties
        self.file_name_congratulation_enrolling = file_name_congratulation_enrolling

    def input_student(self):
        while True:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")

            enrollment_date = self.validate_date_input("Enter enrollment date (yyyy/mm/dd): ")
            birth_day = self.validate_date_input("Enter date of birth (yyyy/mm/dd): ")

            try:
                student  Student(name, surname, email, enrollment_date, birth_day)
                student.add_to_file_enrolled(self.file_name_enrolled)
                print(f"Student {name}, added successfully.")
            except ValueError as e:
                print(e)

            FacultyOperations.congratulations_enrolled(name, surname, "", self.file_name_congratulation_enrolling)

            another = input("Do you want to add another student? (y/n)").lower()
            if another != "y":
                break
            
    def delete_student_by_email(self):
        while True:
            kicked_email = input("Input email of the student you want to kick: ")

            student_found = False
            enrolled_students = self.load_enrolled_students()

            for students in enrolled_students:
                if student["Email"] == kicked_email:
                    student_found = True

            if not student_found:
                print(f"Student with email ''{kicked_email} not found. ")
                continue

            updated_enrolled_students = [student for student in enrolled_students if student['Email'] != kicked_email]
            self.save_enrolled_students(updated_enrolled_students)

            faculties_data = self.load_faculties_data()

            for faculty in faculties_data:
                if kicked_email in faculty["Student1"]:
                    faculty["Student1"].remove(kicked_email)

            self.save_faculties_data(faculties_data)

            print(f"Student with email {kicked_email} was kicked successfully.")
            another = input("Do you want to kick another student? (y/n): ").lower()
            if another != "y":
                break
