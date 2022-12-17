import requests as req
import time
from bs4 import BeautifulSoup as soup


def main():
    # Main URL
    base_url = 'https://finance.yahoo.com'
    url_slug = '/quote/'

    # Ticker symbols
    stocks = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

    response = req.get(base_url)
    print(f'[-] Status code: {response.status_code}')

    for ticker in stocks:
        full_url = base_url+url_slug+ticker
        stock_page = req.get(full_url)
        if stock_page.status_code == 200:
            page_source = stock_page.text
            parsed_page = soup(page_source, 'html.parser')
            try:
                # Price element
                stock_price = parsed_page.find('fin-streamer', attrs={'data-symbol': f'{ticker}'}).text
                print(f'[-] Ticker {ticker} = {stock_price}')
            except:
                print('Error. Cannot Find the Price Element.')
        else:
            print(f'[x] Request to the page {full_url} failed.\n[x] Status code: {stock_page.status_code}')
        time.sleep(2)


if __name__ == '__main__':
    main()
