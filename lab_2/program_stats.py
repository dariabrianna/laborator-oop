import re

def get_program_stats(file_path):
    if file_path.endswith(".py"):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            line_count = len(lines)
            class_count = count_classes(content)
            method_count = count_methods(content)
            word_count = count_words(content)
            char_count = count_characters(content)

        return line_count, class_count, method_count, word_count, char_count
    elif file_path.endswith(".java"):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            line_count = len(lines)
            class_count = count_classes(content)
            method_count = count_methods(content)
            word_count = count_words(content)
            char_count = count_characters(content)

        return line_count, class_count, method_count, word_count, char_count
    return 0, 0, 0, 0, 0

def count_classes(content):
    class_pattern = r'\bclass\b'
    class_count = len(re.findall(class_pattern, content))
    return class_count

def count_methods(content):
    method_pattern = r'\bdef\s+(\w+)\s*\(.*\)\s*:'
    method_count = len(re.findall(method_pattern, content))
    return method_count

def count_words(content):
    words = content.split()
    word_count = len(words)
    return word_count

def count_characters(content):
    char_count = len(content)
    return char_count
