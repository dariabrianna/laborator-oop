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