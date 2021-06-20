"""This script to get links to boxers' profiles on boxrec.com
website.
"""

#  TODO: реализовать doctest
#  TODO: реализовать multiprocessing

import sys

import requests
from requests import ReadTimeout
from requests import HTTPError
from requests import Timeout
from requests import ConnectionError
from requests.exceptions import MissingSchema

from random import choice
from random import uniform
from time import sleep

from bs4 import BeautifulSoup

from secret import secret


SHORT_URL = '/en/proboxer/'
DOMAIN_ROOT = 'https://boxrec.com'


def choice_user_agents() -> str:
    """Return a string random. The string contains data
    of User-Agent.

    Raises IOError if file user_agents.txt not exist.
    """
    try:
        with open('data/user_agents.txt') as user_agents:
            user_agent = choice(user_agents.read().split('\n'))
        return user_agent
    except IOError:
        print('There is no data file data/user_agents.txt to mask the '
              'request.')
        sys.exit()


def cuts_string_containing_url(file='data/data_urls.csv') -> tuple:
    """Returns a tuple of 1 row and the rest of the rows."""
    with open(file, 'r') as f:
        url = f.readline().strip()
        strings = f.readlines()
    return strings, url


def saves_strings(strings: list[str], file='data/data_urls.csv') -> None:
    """Saves strings."""
    with open(file, 'w') as f:
        for string in strings:
            f.write(string)


def connect_via_proxy(url: str, user_agent: str):
    """Trying to establish a successful connection. Proxy changes every
    time you try.
    """
    while True:
        try:
            response = requests.get(
                url,
                headers={'User-Agent': user_agent},
                proxies=secret.SECRET,
                timeout=6)
            return response.text
        except (ConnectionError, HTTPError, ReadTimeout, Timeout):
            sleep(uniform(4, 8))
            continue
        except MissingSchema:
            print('No url for search in file data/test.py')
            sys.exit()


def get_links(data: str) -> list:
    """Get links to boxers' profiles."""
    soup = BeautifulSoup(data, 'lxml')
    links = soup.find_all('a')
    return [link for link in links]


def sort_links(data: list) -> list:
    """The function returns a list with links to boxers' profiles."""
    return [''.join((DOMAIN_ROOT, url)) for url in data if SHORT_URL in url]


def write_csv(data: list) -> None:
    """Write the profile addresses to the file line by line."""
    with open('data/data.csv', 'a') as file:
        for url in data:
            file.write(''.join((url, '\n')))


def main():
    """As long as there are links in the prepared file, the function
    will extract the address from the file, extract the profile links
    from the address and save them to another file.
    """
    while True:
        user_agent = choice_user_agents()
        strings, url = cuts_string_containing_url()
        saves_strings(strings)
        data = connect_via_proxy(url, user_agent)
        data = get_links(data)
        data = sort_links(data)
        write_csv(data)


if __name__ == '__main__':
    main()
