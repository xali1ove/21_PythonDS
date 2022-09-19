#!/usr/local/bin/python3

class Research:

    def file_reader(self) -> str:
        f = open('data.csv', 'r')
        content = f.read()
        f.close()
        return content

def main():

    researcher = Research()
    print(researcher.file_reader())


if __name__ == '__main__':
    main()
