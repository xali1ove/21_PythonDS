#!/usr/local/bin/python3

def read_file(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def write_file(filename: str, lines: list) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def get_csv_string_value(csv_line: str, begin_index: int, sep=',') -> str:
    if csv_line[begin_index] != '"':
        raise ValueError("Can't get csv string value: the value is not a string")

    end_index = csv_line.find('"', begin_index + 1)
    while end_index != -1:
        if (end_index - begin_index > 1) and (csv_line[end_index - 1] == '\\'):
            end_index = csv_line.find('"', end_index + 1)
        else:
            break

    if end_index == -1:
        raise RuntimeError("Syntax error: unclosed quote")

    end_index += 1

    if (end_index + 1 != len(csv_line)) and (csv_line[end_index] != sep):
        raise RuntimeError("Syntax error: separator after quote is missing")

    return csv_line[begin_index:end_index]


def get_csv_any_value(csv_line: str, begin_index: int, sep=',') -> str:
    end_index = csv_line.find(sep, begin_index + 1)

    if end_index == -1:
        return csv_line[begin_index:]

    return csv_line[begin_index:end_index]


def split_csv_line(csv_line: str, sep=',') -> list:
    splitted_line = []

    begin_index = 0
    while begin_index < len(csv_line):
        if csv_line[begin_index] == sep:
            begin_index += 1

        if csv_line[begin_index] == '"':
            value = get_csv_string_value(csv_line, begin_index)
        else:
            value = get_csv_any_value(csv_line, begin_index)

        splitted_line.append(value)

        begin_index += len(value)

    return splitted_line


def main():
    input_lines = read_file('ds.csv')
    output_lines = []

    for line in input_lines:
        output_lines.append('\t'.join(split_csv_line(line)))

    write_file("ds.tsv", output_lines)


if __name__ == '__main__':
    main()