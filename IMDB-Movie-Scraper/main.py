import requests
from bs4 import BeautifulSoup as soup
import json


def main():
    # Get actor name from user input
    actor_name = input("\nEnter the actor name: ")

    # Base URL
    base_url = 'https://www.imdb.com'
    url_slug = '/find?q='
    full_url = base_url+url_slug+actor_name
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}

    print(f'\n{full_url}')

    search_request = requests.get(full_url, headers=my_headers)
    print(f'[-] Status code: {search_request.status_code}')

    search_page = soup(search_request.text, 'html.parser')
    actor_name = search_page.find('a', class_='ipc-metadata-list-summary-item__t').text
    print(f'[-] Actor Name: {actor_name}')
    actor_url_slug = search_page.find('a', class_='ipc-metadata-list-summary-item__t')['href']
    actor_url = base_url+actor_url_slug
    print(f'[-] Actor URL: {actor_url}')

    actor_request = requests.get(actor_url, headers=my_headers)
    print(f'\n[-] Status code: {actor_request.status_code}\n')

    actor_page = soup(actor_request.text, 'html.parser')
    movie_names = actor_page.findAll('a', class_='ipc-metadata-list-summary-item__t')

    for movie in movie_names[:4]:
        print(movie.text)


if __name__ == '__main__':
    main()
