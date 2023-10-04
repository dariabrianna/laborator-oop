from faculty import Faculty

class GeneralOperations:
    def __init__(self, file_name_faculties, file_name_enrolled):
        self.file_name_faculties = file_name_faculties
        self.file_name_enrolled = file_name_enrolled

    def input_faculty(self):
        study_fields = ["Mechanical_Engineering", "Software_Engineering", "Food_Technology", "Urbanism_Architecture",
                        "Veterinary_Medicine"]

        while True:
            Name = input("Enter faculty name: ")
            Abbreviation = input("Enter abbreviation: ")
            print("Available fields: Mechanical_Engineering, Software_Engineering,"
                  " Food_Technology, Urbanism_Architecture, Veterinary_Medicine")
            Study_Field = input("Enter Study_Field: ")
            while Study_Field not in study_fields:
                print("Wrong field, try again")
                Study_Field = input("Enter Study_Field: ")

            try:
                faculty = Faculty(Name, Abbreviation, Study_Field)
                faculty.add_faculty(self.file_name_faculties)
                print(f"Faculty {Name}, added successfully.")
            except ValueError as e:
                print(e)

            another = input("Do you want to add another faculty? (y/n)").lower()
            if another != "y":
                break

    def search_student_what_faculty(self):
        while True:
            student_email = input("Enter the student's email: ")
            student_found = False

            enrolled_students = []
            faculties_data = []

            with open(self.file_name_enrolled, 'r' as enrolled_file) as enrolled_file:
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

                    if student["Email"] == student_email:
                        student_found = True
                        break
                    
            if not student_found:
                print(f"Student with email '{student_email}' not found.")
                continue

            with open(self.file_name_faculties, 'r') as faculties_file:
                for line in faculty_file:
                    faculty_info = line.strip().split(', ')
                    if len(faculty_info) < 4:
                        print("Invalid data in faculties.txt. Please check the file format.")
                        break
                    student1_data = faculty_info[2].split(': ')[1].strip('[]')
                    student1_list = [s.strip() for s in student1_data.split(';') if s.strip()]
                    faculty = Faculty(faculty_info[0].split(': ')[1], faculty_info[1].split(': ')[1], faculty_info[3].split(': ')[1])
                    faculty.Student1 = student1_list  # Assign the list of students to the Faculty object
                    faculties_data.append(faculty)

            faculty_found = False

            for faculty in faculties_data:
                if student_email in faculty.Student1:
                    faculty_found = True
                    print(f"Student with email '{student_email}' is a member of the following faculty:")
                    print(f"- {faculty.name} ({faculty.abbreviation})")

            if not faculty_found:
                print(f"Student with email '{student_email}' is not found in any faculty.")

            another = input("Do you want to search another student? (yes/no): ").lower()
            if another != "yes":
                break
