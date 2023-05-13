import re


def process_file(file_path, output_file, language_code, num_records=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if num_records is not None:
        lines = lines[:num_records]

    new_lines = []
    for line in lines:
        line = line.strip()
        line = line.lower()
        line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
        line = re.sub(r'^\d+\t\w+\t', f'__label__{language_code}\t', line)

        new_lines.append(line)

    with open(output_file, 'a', encoding='utf-8') as file:
        file.write('\n'.join(new_lines))


def process_test_set(input_file, output_file, language_code, num_records=None):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if num_records is not None:
        lines = lines[-num_records:]

    new_lines = []
    for line in lines:
        line = line.strip()
        line = line.lower()
        line = re.sub(r'[^a-zA-Z0-9\s]', '', line)
        line = re.sub(r'^\d+\t\w+\t', f'__label__{language_code}\t', line)
        new_lines.append(line)

    with open(output_file, 'a', encoding='utf-8') as file:
        file.write('\n'.join(new_lines))
