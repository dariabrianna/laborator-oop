class Faculty:
    def __init__(self, Name, Abbreviation, Study_Field):
        self.Name = Name
        self.Abbreviation = Abbreviation
        self.Student1 = []
        self.Study_Field = Study_Field

    def add_faculty(self, file_name):
        faculty_info = self.change_to_string()  # Get the faculty's info as a formatted string

        with open(file_name, 'a') as file:
            file.write(faculty_info + '\n')  # Write the faculty's info as a line in the file

    def change_to_string(self):
        # Convert the student object to a formatted string
        faculties_str = (f'{{Name: {self.Name},'
                         f' Abbreviation: {self.Abbreviation},'
                         f' Student1: {self.Student1}, '
                         f'Study_Field: {self.Study_Field}}}'
                         )
        return faculties_str