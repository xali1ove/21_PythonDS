#!/usr/local/bin/python3

import sys


def get_subjects_data() -> tuple:

    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    return COMPANIES, STOCKS


def process_stocks_request(ticker_symbol: str) -> None:
    companies, stocks = get_subjects_data()

    ticker_symbol = ticker_symbol.upper()
    if ticker_symbol in stocks:
        company_name = list(companies.keys())[list(companies.values()).index(ticker_symbol)]
        print(company_name, stocks[ticker_symbol])
    else:
        print('Unknown ticker')


def main():
    if len(sys.argv) == 2:
        process_stocks_request(sys.argv[1])


if __name__ == '__main__':
    main()