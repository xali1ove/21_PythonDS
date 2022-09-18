#!/usr/local/bin/python3

import sys

def read_file(filename: str) -> list:

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_file(filename: str, lines: list) -> None:

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def email_extract_names(email: str) -> tuple:

    dot_index = email.find('.')
    at_sign_index = email.find('@')

    name = email[:dot_index]
    name = str.upper(name[0]) + name[1:]

    surname = email[dot_index + 1:at_sign_index]
    surname = str.upper(surname[0]) + surname[1:]

    return (name, surname)


def extract_names_to_csv(emails: list) -> list:

    tsv_data = ['"Name"\t"Surname"\t"E-mail"\n']

    for email in emails:
        email = email.replace('\n', '')
        extracted = email_extract_names(email)
        tsv_data.append(f'"{extracted[0]}"\t"{extracted[1]}"\t"{email}"\n')

    return tsv_data

def main():

    if len(sys.argv) == 2:
        data = extract_names_to_csv(read_file(sys.argv[1]))
        write_file('employees.tsv', data)


if __name__ == '__main__':
    main()