#!/usr/local/bin/python3

class Must_read:
    f = open('data.csv', 'r')
    content = f.read()
    print(content)
    f.close()
