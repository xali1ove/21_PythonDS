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


def process_stocks_request(company_name: str) -> None:
    companies, stocks = get_subjects_data()

    company_name = company_name.lower()
    for company, ticker_symbol in companies.items():
        if company_name == company.lower():
            print(stocks.get(ticker_symbol))
            return

    print('Unknown company')


def main():
    if len(sys.argv) == 2:
        process_stocks_request(sys.argv[1])


if __name__ == '__main__':
    main()
