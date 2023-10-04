from student import Student
from faculty_func import FacultyOperations

class StudentOperations:
    def __init__(self, file_name_enrolled, file_name_faculties, file_name_congratulation_enrolling):
        self.file_name_enrolled = file_name_enrolled
        self.file_name_faculties = file_name_faculties
        self.file_name_congratulation_enrolling = file_name_congratulation_enrolling

    def input_student(self):
        while True:
            name = input("Enter first name: ")
            surname = input("Enter last name: ")
            email = input("Enter email: ")

            enrollment_date = self.validate_date_input("Enter enrollment date (yyyy/mm/dd): ")
            birth_day = self.validate_date_input("Enter date of birth (yyyy/mm/dd): ")

            try:
                student = Student(name, surname, email, enrollment_date, birth_day)
                student.add_to_file_enrolled(self.file_name_enrolled)
                print(f"Student {name}, added successfully.")
            except ValueError as e:
                print(e)

            FacultyOperations.graduate_student(name, surname, "", self.file_name_congratulation_enrolling)

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

    def validate_date_input(self, message):
        while True:
            date = input(message)
            try:
                Student.correct_format_date(date)
                return date
            except ValueError as e:
                print(e)

    def load_enrolled_students(self):
        enrolled_students = []
        with open(self.file_name_enrolled, 'r') as enrolled_file:
            for line in enrolled_file:
                student_info = line.strip().split(', ')
                student = {
                    'First name': student_info[0].split(': ')[1],
                    'Last name': student_info[1].split(': ')[1],
                    'Email': student_info[2].split(': ')[1],
                    'Enrollment date': student_info[3].split(': ')[1],
                    'Date of birth': student_info[4].split(': ')[1]
                }
                enrolled_students.append(student)
        return enrolled_students

    def save_enrolled_students(self, enrolled_students):
        with open(self.file_name_enrolled, 'w') as enrolled_file:
            for student in enrolled_students:
                enrolled_file.write(f"{{First name: {student['First name']}, Last name: {student['Last name']}, Email: {student['Email']}, Enrollment date: {student['Enrollment date']}, Date of birth: {student['Date of birth']}\n")

    def load_faculties_data(self):
        faculties_data = []
        with open(self.file_name_faculties, 'r') as faculty_files:
            for line in faculty_file:
                faculty_info = line.strip().split(', ')
                if len(faculty_info) < 4:
                    print("Invalid data in faculties.txt. Please check the file format.")
                    break
                student1_data = faculty_info[2].split(': ')[1].strip('[]')
                student1_list = [s.strip() for s in student1_data.split(';') if s.strip()]
                faculty = {
                    'Name': faculty_info[0].split(': ')[1],
                    'Abbreviation': faculty_info[1].split(': ')[1],
                    'Student1': student1_list,
                    'Study_Field': faculty_info[3].split(': ')[1]
                }
                
                faculties_data.append(faculty)
        return faculties_data

        # Helper method to save faculty data to file
    def save_faculties_data(self, faculties_data):
        with open(self.file_name_faculties, 'w') as faculty_file:
            for faculty in faculties_data:
                students_str = '; '.join(faculty['Student1'])
                faculty_file.write(
                    f"Name: {faculty['Name']}, Abbreviation: {faculty['Abbreviation']}, Student1: [{students_str}], Study_Field: {faculty['Study_Field']}\n")

