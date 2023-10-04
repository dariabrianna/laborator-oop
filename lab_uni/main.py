class University:
    def init(self, faculties):
        self.faculties = faculties

faculties_data = {}
class Faculty:
    def init(self, name, abbreviation, study_field):
        self.name = name
        self. abbreviation = abbreviation
        swlf.study_field = study_field

    def add_to_university(self):
        faculties_data[self.name] = []

class Student:
    def init(self, name, surname, email, birth_year, birth_month, birth_day, enrollment_year, enrollment_month, enrollment_day, graduation_status, faculty):
        self.name = name
        self.surname = surname
        self.email = email
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.enrollment_year = enrollment_year
        self.enrollment_month = enrollment_month
        self.enrollment_day = enrollment_day
        self.graduation_status = graduation_status
        self.faculty = faculty

    def add_student_to_faculty(self):
        if self.faculty in faculties_data:
            faculties_data[self.faculty].append([self.name, self.surname, slef.birth_year, self.birth_month, self.birth_day, self.enrollment_year, self.enrollment_month, self.enrollment_day, self.graduation_status, self.faculty])
        else:
            print(f"Faculty '{self.faculty}' does not exist.")

students_data = []
faculties_list = []
student_index = -1
faculty_index = -1

def find_student(faculties_data, student_email):
    for faculty_name, students in faculties_data.items():
        for student in students:
            if student_email in student:
                print(f"{student[0]} is studying at {faculty_name}")

def place_truth(student_email, student_faculty):
    for i in range(len(students_data)):
        if students_data[i].email == student_email and students_data[i].faculty == student_faculty:
            print(f"{students_data[i].name} is at {students_data[i].faculty}")

def list_faculties(faculties_data):
    for faculty_name in faculties_data.keys():
        print(faculty_name)

def list_enrolled_students(students_data):
    for student in students_data:
        if student.graduation_status == 'not_graduated':
            print(student.name)

def list_graduated_students(students_data):
    for student in students_data:
        if student.graduation_status == 'graduated':
            print(student.name)

def list_faculties_field(field, faculties_list):
    for faculty in faculties_list:
        if faculty.study_field == field:
            print(faculty.name)

while True:
    print("Choose from the following options: ")
    print("f - Faculty operations")
    print("s - Student operations")
    print("g - General operations")
    print("q - Quit program")
    option = input("Enter option: ")

    if option == 's':
        print("What do you want to do?")
        print("ns - Create student")
        sub_option = input("Enter suboption: ")

    if sub_option == 'ns':
        student_index += 1
        students_data.append(None)
        print("Enter Student Name:")
        name = input("Name: ")
        print("Enter Student Surname: ")
        surname = input("Surname: ")
        print("Enter Student email: ")
        email = input("Email: ")
        print("Enter Student Date of birth")
        birth_year = int(input("Year: "))
        birth_month = int(input("Month: "))
        birth_day = int(input("Day: "))
        print("Enter Student date of enrollment ")
        enrollment_year = int(input("Year :"))
        enrollment_month = int(input("Month: "))
        enrollment_day = int(input("Day: "))
        graduation_status = input("Choose 'gratuated' or 'not_graduated': ")
        faculty = input("Faculty: ")

        students_data[student_index] = Student(name, surname, email, birth_year, birth_month, birth_day, enrollment_year, enrollment_month, enrollment_day, graduation_status, faculty)
        students_data[student_index].add_student_to_faculty()

    elif option == 'f':
        print("What do you want to do?")
        print("nf - Create faculty")
        print("ss - Search student and show faculty")
        print("gf - Graduate a student from a faculty")
        sub_option = input("Enter suboption")

        if sub_option == "nf":
            faculty_index += 1
            faculties_list.append(None)
            print("Enter faculty name: ")
            name = input("Name: ")
            print("Enter Faculty abreviation: ")
            abbreviation = input("Abbreviation: ")
            print("Enter Faculty studyField")
            study_field = input("studyField: ")
            faculties_list[faculty_index] = Faculty(name, abbreviation, study_field)
            faculties_list[faculty_index].add_to_university()
            UTM = University(faculties_data)

    elif sub_option = 'ss':
        student_email = input("Enter stdudent email: ")
        find_student(faculties_data, student_email)

    elif sub_option == 'gf':
        student_name = input("Enter the name of the student to graduate: ")
        for student in students_data:
            if student.name == student_name:
                if student.graduation_status == "not_graduated":
                    stdudent.graduation_status = "graduated"
                    print(f"Now, {stdudent.name} is graduated ! ! !")
                    
