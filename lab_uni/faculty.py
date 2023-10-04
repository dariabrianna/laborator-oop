class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.first_Student = []
        self.study_field = study_field

    def add_faculty(self, file_name):
        faculty_info = self.to_dict_as_str()  # Get the faculty's info as a formatted string

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