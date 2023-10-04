from faculty import Faculty

class FacultyOperations:
    def __init__(self, faculties_file, enrolled_file, graduates_file, enrolling_congrats_file, graduating_congrats_file):
        self.faculties_file = faculties_file
        self.enrolled_file = enrolled_file
        self.graduates_file = graduates_file
        self.enrolling_congrats_file = enrolling_congrats_file
        self.graduating_congrats_file = graduating_congrats_file

    def add_student(self):
        while True:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")

            # Validate enrollment date and date of birth
            while True:
                enrollment_date = input("Enter enrollment date (yyyy/mm/dd): ")
                try:
                    validate_date_input(enrollment_date)
                    break
                except ValueError as e:
                    print(e)

            while True:
                # Check date of birth
                date_of_birth = input("Enter date of birth (yyyy/mm/dd): ")
                try:
                    validate_date_input(date_of_birth)
                    break
                except ValueError as e:
                    print(e)

            try:
                student = Student(first_name, last_name, email, enrollment_date, date_of_birth)
                student.add_to_enrolled_file(self.enrolled_file)
            except ValueError as e:
                print(e)

            faculty_abbr = input("Enter the faculty abbreviation: ")

            # Check faculty existence
            faculty_found = False
            faculties_data = []

            with open(self.faculties_file, 'r') as faculty_file:
                for line in faculty_file:
                    faculty_info = line.strip().split(', ')
                    if len(faculty_info) < 4:
                        print("Invalid data in faculties.txt. Please check the file format.")
                        break
                    student_emails_data = faculty_info[2].split(': ')[1].strip('[]')
                    student_emails_list = [s.strip() for s in student_emails_data.split(';') if s.strip()]
                    faculty = {
                        'Name': faculty_info[0].split(': ')[1],
                        'Abbreviation': faculty_info[1].split(': ')[1],
                        'Student_Emails': student_emails_list,
                        'Study_Field': faculty_info[3].split(': ')[1]
                    }

                    faculties_data.append(faculty)

                    if faculty["Abbreviation"] == faculty_abbr:
                        faculty_found = True
                        break

            if not faculty_found:
                print("Faculty does not exist, try again!")
                continue

            student_email = email

            # Find the faculty data in faculties_data
            faculty_data = None
            for faculty in faculties_data:
                if faculty["Abbreviation"] == faculty_abbr:
                    faculty_data = faculty
                    break

            if faculty_data is None:
                print(f"Faculty with abbreviation '{faculty_abbr}' not found.")
                continue

            faculty_data.setdefault("Student_Emails", []).append(student_email)

            # Save the updated faculty data back to faculties.txt
            with open(self.faculties_file, 'w') as faculty_file:
                for faculty in faculties_data:
                    students_str = '; '.join(faculty['Student_Emails'])
                    faculty_file.write(
                        f"{{Name: {faculty['Name']}, Abbreviation: {faculty['Abbreviation']}, Student_Emails: [{students_str}], Study_Field: {faculty['Study_Field']}\n")

            # Load student data from current_enrolled_students.txt
            student_data = None
            with open(self.enrolled_file, 'r') as enrolled_file:
                for line in enrolled_file:
                    student_info = line.strip().split(', ')
                    if len(student_info) < 5:
                        print("Invalid data in current_enrolled_students.txt. Please check the file format.")
                        break
                    student = {
                        'First name': student_info[0].split(': ')[1],
                        'Last name': student_info[1].split(': ')[1],
                        'Email': student_info[2].split(': ')[1],
                        'Enrollment date': student_info[3].split(': ')[1],
                        'Date of birth': student_info[4].split(': ')[1]
                    }
                    if student["Email"] == student_email:
                        student_data = student
                        break

            if student_data is None:
                print(f"Student with email '{student_email}' not found.")
                continue

            print(f"Student {first_name}, added and assigned successfully.")
            self.congratulations_enrolled(first_name, last_name, faculty_data['Name'], enrollment_date, self.enrolling_congrats_file)
            another = input("Do you want to add and assign another student? (yes/no): ").lower()
            if another != "yes":
                break

    def assign_student_to_faculty(self):
        while True:
            faculty_abbr = input("Enter the faculty abbreviation: ")

            # Check faculty existence
            faculty_found = False
            faculties_data = []

            with open(self.faculties_file, 'r') as faculty_file:
                for line in faculty_file:
                    faculty_info = line.strip().split(', ')
                    faculty = {
                        'Name': faculty_info[0].split(': ')[1],
                        'Abbreviation': faculty_info[1].split(': ')[1],
                        'Student_Emails': [s.strip() for s in faculty_info[2].split(': ')[1].strip('[]').split(';') if s.strip()],
                        'Study_Field': faculty_info[3].split(': ')[1]
                    }
                    faculties_data.append(faculty)

                    if faculty["Abbreviation"] == faculty_abbr:
                        faculty_found = True

            if not faculty_found:
                print("Faculty does not exist, try again!")
                continue

            student_email = input("Enter the student's email: ")

            # Find the faculty data in faculties_data
            faculty_data = None
            for faculty in faculties_data:
                if faculty["Abbreviation"] == faculty_abbr:
                    faculty_data = faculty
                    break

            if faculty_data is None:
                print(f"Faculty with abbreviation '{faculty_abbr}' not found.")
                continue

            faculty_data.setdefault("Student_Emails", []).append(student_email)

            # Save the updated faculty data back to faculties.txt
            with open(self.faculties_file, 'w') as faculty_file:
                for faculty in faculties_data:
                    students_str = '; '.join(faculty['Student_Emails'])
                    faculty_file.write(
                        f"{{Name: {faculty['Name']}, Abbreviation: {faculty['Abbreviation']}, Student_Emails: [{students_str}], Study_Field: {faculty['Study_Field']}\n")

            print(f"Student with email '{student_email}' added successfully to faculty '{faculty_abbr}'.")

    def graduate_student(self):
        while True:
            graduated_email = input("Enter the student's email: ")

            # Check student existence
            student_found = False
            enrolled_students = []

            with open(self.enrolled_file, 'r') as enrolled_file:
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

                    if student["Email"] == graduated_email:
                        student_found = True

            if not student_found:
                print(f"Student with email '{graduated_email}' not found.")
                continue

            # Remove the graduated student from the list of enrolled students
            updated_enrolled_students = [student for student in enrolled_students if student['Email'] != graduated_email]

            # Save the updated list back to current_enrolled_students.txt
            with open(self.enrolled_file, 'w') as enrolled_file:
                for student in updated_enrolled_students:
                    enrolled_file.write(
                        f"{{First name: {student['First name']}, Last name: {student['Last name']}, Email: {student['Email']}, Enrollment date: {student['Enrollment date']}, Date of birth: {student['Date of birth']}\n")

            faculties_data = []  # List to store faculty information
            # Load faculty data
            with open(self.faculties_file, 'r') as faculty_file:
                for line in faculty_file:
                    faculty_info = line.strip().split(', ')
                    if len(faculty_info) < 4:
                        print("Invalid data in faculties.txt. Please check the file format.")
                        break
                    student_emails_data = faculty_info[2].split(': ')[1].strip('[]')
                    student_emails_list = [s.strip() for s in student_emails_data.split(';') if s.strip()]
                    faculty = {
                        'Name': faculty_info[0].split(': ')[1],
                        'Abbreviation': faculty_info[1].split(': ')[1],
                        'Student_Emails': student_emails_list,
                        'Study_Field': faculty_info[3].split(': ')[1]
                    }
                    faculties_data.append(faculty)

            # Save the updated faculties data back to faculties.txt
            with open(self.faculties_file, 'w') as faculty_file:
                # Iterate through faculties and remove the graduated student from their lists
                for faculty in faculties_data:
                    if graduated_email in faculty.get("Student_Emails", []):
                        faculty["Student_Emails"].remove(graduated_email)
                    students_str = '; '.join(faculty['Student_Emails'])
                    faculty_file.write(
                        f"{{Name: {faculty['Name']}, Abbreviation: {faculty['Abbreviation']}, Student_Emails: [{students_str}], Study_Field: {faculty['Study_Field']}\n")

            # Move the graduated student to graduated_students.txt
            graduated_students_data = []
            with open(self.graduates_file, 'r') as graduated_file:
                for line in graduated_file:
                    student_info = line.strip().split(', ')
                    student = {
                        'First name': student_info[0].split(': ')[1],
                        'Last name': student_info[1].split(': ')[1],
                        'Email': student_info[2].split(': ')[1],
                        'Enrollment date': student_info[3].split(': ')[1],
                        'Date of birth': student_info[4].split(': ')[1]
                    }
                    graduated_students_data.append(student)

            # Find the student data in enrolled students
            graduated_student_data = next((student for student in enrolled_students if student['Email'] == graduated_email), None)

            # Add the graduated student data to the graduated students list
            if graduated_student_data:
                graduated_students_data.append(graduated_student_data)

            # Save the updated list to graduated_students.txt
            with open(self.graduates_file, 'w') as graduated_file:
                for student in graduated_students_data:
                    graduated_file.write(
                        f"{{First name: {student['First name']}, Last name: {student['Last name']}, Email: {student['Email']}, Enrollment date: {student['Enrollment date']}, Date of birth: {student['Date of birth']}\n")

            while True:
                graduated_date = input("Enter graduated date (yyyy/mm/dd): ")
                try:
                    validate_date_input(graduated_date)
                    break
                except ValueError as e:
                    print(e)
            print("Student graduated successfully!")
            self.congratulations_enrolled(graduated_student_data['First name'], graduated_student_data['Last name'], faculty['Name'], graduated_date, self.graduating_congrats_file)

            another = input("Do you want to graduate another student? (yes/no): ").lower()
            if another != "yes":
                break

    def display_enrolled_students(self):
        try:
            with open(self.enrolled_file, 'r') as enrolled_file:
                for line in enrolled_file:
                    # Remove extra brackets at the beginning and end
                    line = line.strip()[1:-1]
                    enrolled_data = {}
                    # Split the line by commas to separate key-value pairs
                    key_value_pairs = line.strip().split(', ')
                    for pair in key_value_pairs:
                        key, value = pair.split(': ')
                        enrolled_data[key] = value
                    print("First name:", enrolled_data.get("First name"))
                    print("Last name:", enrolled_data.get("Last name"))
                    print("Email:", enrolled_data.get("Email"))
                    print("Enrollment date:", enrolled_data.get("Enrollment date"))
                    print("Date of birth:", enrolled_data.get("Date of birth"))
                    print()
        except FileNotFoundError:
            print(f"The '{self.enrolled_file}' file does not exist.")

    def display_graduated_students(self):
        try:
            with open(self.graduates_file, 'r') as graduates_file:
                for line in graduates_file:
                    # Remove extra brackets at the beginning and end
                    line = line.strip()[1:-1]
                    graduates_data = {}
                    # Split the line by commas to separate key-value pairs
                    key_value_pairs = line.strip().split(', ')
                    for pair in key_value_pairs:
                        key, value = pair.split(': ')
                        graduates_data[key] = value
                    print("First name:", graduates_data.get("First name"))
                    print("Last name:", graduates_data.get("Last name"))
                    print("Email:", graduates_data.get("Email"))
                    print("Enrollment date:", graduates_data.get("Enrollment date"))
                    print("Date of birth:", graduates_data.get("Date of birth"))
                    print()
        except FileNotFoundError:
            print(f"The '{self.graduates_file}' file does not exist.")
