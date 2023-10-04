class Student:
    def __init__(self, name, surname, email, birth_day, enrollment_date):
        self.name = name
        self.surname = surname
        self.email = email
        self.birth_day = birth_day
        self.enrollment_date = enrollment_date

    @staticmethod
    def correct_format_date(date_str):
        parts = date_str.split('/')
        
        if len(parts) != 3:
            raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

        try:
            year, month, day = map(int, parts)

            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

            return year, month, day
        except (ValueError, TypeError):
            raise ValueError("Invalid date format. Please use yyyy/mm/dd.")

    def change_to_string(self):
        student_dict = {
            'First name': self.name,
            'Last name': self.surname,
            'Email': self.email,
            'Enrollment date': self.enrollment_date,
            'Date of birth': self.birth_day
        }
        student_str = ', '.join([f'{key}: {value}' for key, value in student_dict.items()])
        return f'{{{student_str}}}'

    def add_to_file_enrolled(self, file_name):
        student_info = self.change_to_string()  # Get the student's info as a formatted string

        with open(file_name, 'a') as file:
            file.write(student_info + '\n')
