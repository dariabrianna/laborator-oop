class University:
#             txt_file.write(f"    Student: {', '.join(map(str, student_info))}\n")
    def __init__(self):
        self.file_name_enrolled = "enrolled_students.txt"
        self.file_name_faculties = "faculties.txt"
        self.file_name_graduates = "graduated_students.txt"
        self.file_name_congratulation_enrolling = "message_enroll.txt"
        self.file_name_congratulation_graduating = "message_graduate.txt"
        self.general_manager = GeneralOperations(self.file_name_faculties, self.file_name_enrolled)
        self.faculty_manager = FacultyOperations(self.file_name_faculties, self.file_name_enrolled,
                                                 self.file_name_graduates, self.file_name_congratulation_enrolling,
                                                 self.file_name_congratulation_graduating)
        self.student_manager = StudentOperations(self.file_name_enrolled, self.file_name_faculties,
                                                 self.file_name_congratulation_enrolling)
