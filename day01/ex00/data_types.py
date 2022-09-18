#!/usr/local/bin/python3

def data_types():
    variables: tuple = (
        1,
        'some text',
        4.2,
        True,
        [1, 2, 3, '100'],
        {'first': 1, 'second': 2},
        (1, 'asd', True),
        {1, 5, 3, 4, 6}
    )

    output = '['
    for var in variables:
        output += type(var).__name__ + ', '
    output = output[:-2] + ']'

    print(output)


if __name__ == '__main__':
    data_types()