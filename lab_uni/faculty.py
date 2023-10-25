class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.study_field = study_field

    def add_to_file_faculties(self, file_name):
        faculty_info = self.to_dict_as_str()  # Get the faculty's info as a formatted string

        with open(file_name, 'a') as file:
            file.write(faculty_info + '\n')  # Write the faculty's info as a line in the file

    def to_dict_as_str(self):
        # Convert the student object to a formatted string
        faculty_str = (f'{{Name: {self.name},'
                       f' Abbreviation: {self.abbreviation},'
                       f' Students: {self.students}, '
                       f'Study_Field: {self.study_field}}}'
                       )
        return faculty_str
