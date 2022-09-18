import sys

def data() :
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

def search_by_key(company: str) -> bool:
    COMPANIES, STOCKS = data()
    comp = ''
    if company.lower().capitalize() not in COMPANIES:
        return False
    else:
        for val in COMPANIES:
            if company.lower().capitalize() == val:
                comp = COMPANIES[val]
        for val in STOCKS:
            if comp == val:
                print(company.lower().capitalize(), "stock price is", STOCKS[val])
                return True

def search_by_value(search: list) -> bool:
    COMPANIES, STOCKS = data()
    if search.upper() not in STOCKS:
        return False
    else:
        for key, value in COMPANIES.items():
            if value == search.upper():
                print(search.upper(), "is a ticker symbol for", key)
                return True

def search_by_value_and_by_key(search: list) -> None:
    for line in search:
        if not search_by_key(line) and not search_by_value(line):
            print(line.lower().capitalize(), "is an unknown company or an unknown ticker symbol")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        search = sys.argv[1].replace(" ", '').split(',')
        if '' not in search:
            search_by_value_and_by_key(search)
