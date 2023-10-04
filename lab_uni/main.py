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

