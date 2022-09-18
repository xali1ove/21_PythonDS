#!/usr/local/bin/python3

def get_subjects_data() -> list:

    country_codes_dict = {
        'Russia': '25',
        'France': '132',
        'Germany': '132',
        'Spain': '178',
        'Italy': '162',
        'Portugal': '17',
        'Finland': '3',
        'Hungary': '2',
        'The Netherlands': '28',
        'The USA': '610',
        'The United Kingdom': '95',
        'China': '83',
        'Iran': '76',
        'Turkey': '65',
        'Belgium': '34',
        'Canada': '28',
        'Switzerland': '26',
        'Brazil': '25',
        'Austria': '14',
        'Israel': '12'
    }

    return country_codes_dict


def sort_dictionary(dictionary: dict) -> dict:

    return dict(sorted(dictionary.items(),
                        key=lambda item: (-int(item[1]), item[0])))


def pretty_print(dictionary: dict) -> None:
    for country in dictionary.keys():
        print(country)


def main():
    sorted_dict = sort_dictionary(get_subjects_data())
    pretty_print(sorted_dict)


if __name__ == '__main__':
    main()