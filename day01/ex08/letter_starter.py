#!/usr/local/bin/python3

import sys

def read_file(filename: str) -> list:

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_file(filename: str, lines: list) -> None:

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def get_letter_start(email: str, emails_tsv_data: list) -> str:
    found = False

    for tsv_line in emails_tsv_data[1:]:
        tsv_line = tsv_line.replace('\n', '')
        fields = tsv_line.split('\t')
        if fields[2] == f'"{email}"':
            found = True
            break

    if not found or fields[2] != f'"{email}"':
        raise RuntimeError("Such email was not found")

    return f'Dear {fields[0][1:-1]}, welcome to our team. ' + \
            'We are sure that it will be a pleasure to work with you. ' + \
            'That’s a precondition for the professionals that our company hires.'

def main():
    """Main function"""
    if len(sys.argv) == 2:
        data = get_letter_start(sys.argv[1], read_file('employees.tsv'))
        print(data)

if __name__ == '__main__':
    main()