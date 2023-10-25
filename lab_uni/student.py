class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, date_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_birth = date_birth

    @staticmethod
    def validate_date(date_str):
        try:
            year, month, day = map(int, date_str.split('/'))

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

            return year, month, day
        except (ValueError, TypeError):
            raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

    def to_dict_as_str(self):
        # Convert the student object to a custom formatted string
        student_str = (
            f'{{First name: {self.first_name}, '
            f'Last name: {self.last_name}, '
            f'Email: {self.email}, '
            f'Enrollment date: {self.enrollment_date}, '
            f'Date of birth: {self.date_birth}}}'
        )
        return student_str

    def add_to_file_enrolled(self, file_name):
        student_info = self.to_dict_as_str()  # Get the student's info as a formatted string

        with open(file_name, 'a') as file:
            file.write(student_info + '\n')
