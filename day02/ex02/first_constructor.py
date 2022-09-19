import sys
import os


class Research:
    def __init__(self, path: str) -> None:
        self.path = path

    def __chech_header(self, header: str) -> bool:
        if not header:
            return False
        header_list = header.split(",")
        if (len(header_list)) != 2:
            return False
        if len(header_list[0].replace(" ", "")) == 0 or header_list[1] == '\n':
            return False
        return True

    def __chek_lines(self, line: str) -> bool:
        valid = [['1', '0'], ['0', '1']]
        line_list = line.replace("\n", '').split(',')
        if len(line_list) != 2:
            return False
        return line_list in valid

    def file_reader(self) -> str:
        if not os.access(self.path, os.F_OK):
            raise FileNotFoundError(self.path)
        if not os.access(self.path, os.R_OK):
            raise PermissionError("Permission denied ", self.path)
        text = ''
        with open(self.path, 'r') as file:
            header = file.readline()
            if not self.__chech_header(header):
                raise ValueError("Incorrect format header")
            text += header
            i = 0
            for line in file:
                if not self.__chek_lines(line):
                    raise ValueError("Incorrect format csv line")
                text += line
                i += 1
            if i == 0:
                raise ValueError("Incorrect format csv line")
        file.close()
        return text


def main():
    if (len(sys.argv)) == 2:
        try:
            res = Research(sys.argv[1])
            print(res.file_reader())
        except (ValueError, PermissionError) as err:
            print(type(err).__name__, err, sep=': ')
    else:
        print("Wrong number of parameters")


if __name__ == "__main__":
    main()
