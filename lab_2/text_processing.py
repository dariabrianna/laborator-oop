def get_text_stats(file_path):
    if file_path.endswith(".txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                lines = content.split('\n')
                words = content.split()
                char_count = len(content)
                line_count = len(lines)
                word_count = len(words)
                return line_count, word_count, char_count
        except Exception as e:
            return "Error: " + str(e)
    else:
        return "Not a text file"
