import re


def process_file(file_path, language_code, num_records=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if num_records is not None:
        lines = lines[:num_records]

    new_lines = []
    for line in lines:
        line = line.strip()
        line = re.sub(r'^\d+\t\w+\t', f'__label__{language_code}\t', line)
        new_lines.append(line)

    with open('static/combined.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join(new_lines))
