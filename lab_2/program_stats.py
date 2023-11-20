import re

class ProgramFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.line_count = 0
        self.class_count = 0
        self.method_count = 0
        self.word_count = 0
        self.char_count = 0

    def analyze_content(self, content):
        lines = content.split('\n')
        self.line_count = len(lines)
        self.class_count = self.count_classes(content)
        self.method_count = self.count_methods(content)
        self.word_count = self.count_words(content)
        self.char_count = self.count_characters(content)

    def count_classes(self, content):
        class_pattern = r'\bclass\b'
        class_count = len(re.findall(class_pattern, content))
        return class_count

    def count_methods(self, content):
        method_pattern = r'\bdef\s+(\w+)\s*\(.*\)\s*:'
        method_count = len(re.findall(method_pattern, content))
        return method_count

    def count_words(self, content):
        words = content.split()
        word_count = len(words)
        return word_count

    def count_characters(self, content):
        char_count = len(content)
        return char_count

    def count_methods(self, content):
        python_method_pattern = r'\bdef\s+(\w+)\s*\(.*\)\s*:'
        python_method_count = len(re.findall(python_method_pattern, content))

        
        java_method_pattern = r'\b(?:public|private|protected|static|\s)\s+(\w+\s+){1,2}(\w+)\s*\([^)]*\)\s*{'
        java_method_count = len(re.findall(java_method_pattern, content))

        return python_method_count + java_method_count



class PythonFile(ProgramFile):
    def analyze_content(self, content):
        super().analyze_content(content)
        # here we are using inheritance classes inherit the attributes and methods from the ProgramFile class.

class JavaFile(ProgramFile):
    def analyze_content(self, content):
        super().analyze_content(content)


def get_program_stats(file_path):
    if file_path.endswith(".py"):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            python_file = PythonFile(file_path)
            python_file.analyze_content(content)
            return python_file.line_count, python_file.class_count, python_file.method_count, python_file.word_count, python_file.char_count
    elif file_path.endswith(".java"):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            java_file = JavaFile(file_path)
            java_file.analyze_content(content)
            return java_file.line_count, java_file.class_count, java_file.method_count, java_file.word_count, java_file.char_count
    return 0, 0, 0, 0, 0
    #The function takes a file path, opens the file, reads its content, and creates an instance of either PythonFile or JavaFile based on the file extension.