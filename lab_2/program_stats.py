
import re  

def get_program_stats(file_path):
    if file_path.endswith(".py"):
        # Analyze Python file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            line_count = len(lines)
            class_count = count_classes(content)  
            method_count = count_methods(content)  
        return line_count, class_count, method_count

    elif file_path.endswith(".java"):
        # Analyze Java file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            line_count = len(lines)
            class_count = count_classes(content) 
            method_count = count_methods(content)  

        return line_count, class_count, method_count

    return 0, 0, 0
