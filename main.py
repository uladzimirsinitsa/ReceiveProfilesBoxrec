
import requests
from requests import ReadTimeout, HTTPError, Timeout, ConnectionError
from requests.exceptions import MissingSchema

from bs4 import BeautifulSoup

from random import choice
from time import sleep
from random import uniform

from secret import secret


def choice_user_agents():
    """Selects a line from a file in a random order with a data line, agent user"""
    with open('data/user_agents.txt') as user_agents:
        user_agent = choice(user_agents.read().split('\n'))
    return user_agent


def pick_up_remove_line_from_file():
    """Extracts the web page address from the file line by line, saves the updated file without this address"""
    with open('data/test.csv', 'r') as file:
        url = file.readline().strip()
        lines = file.readlines()
    with open('data/test.csv', 'w') as file:
        for line in lines:
            if url not in lines:
                file.write(line)
    return url


def connect_via_proxy(url: str, user_agent: str):
    """Trying to establish a successful connection. Proxy changes every time you try"""
    while True:
        try:
            response = requests.get(url, headers={'User-Agent': user_agent}, proxies=secret.SECRET, timeout=7)
            return response.text
        except (ConnectionError, HTTPError, ReadTimeout, Timeout):
            sleep(uniform(4, 8))
            continue
        except MissingSchema:
            print('No url for search in file data/test.py')
            quit()


def get_all_links(content: str):
    """Get links to boxers' profiles"""
    soup = BeautifulSoup(content, 'lxml')
    links = soup.find_all('a')
    all_links = []
    for link in links:
        link = link.get('href')
        all_links.append(link)
    return all_links


def sort_links(all_links: list):
    """The function returns a list with links to boxers' profiles"""
    clear_data = []
    for link in all_links:
        if str(link)[:13] == "/en/proboxer/":
            clear_data.append('https://boxrec.com' + link)
    return clear_data


def write_csv(clear_data: list):
    """Write the profile addresses to the file line by line"""
    with open('data/data.csv', 'a') as file:
        for line in clear_data:
            file.write(line + '\n')


def main():
    """As long as there are links in the prepared file, the function will extract the address from the file,
    extract the profile links from the address and save them to another file."""
    while True:
        user_agent = choice_user_agents()
        url = pick_up_remove_line_from_file()
        content = connect_via_proxy(url, user_agent)
        all_links = get_all_links(content)
        clear_data = sort_links(all_links)
        write_csv(clear_data)


if __name__ == '__main__':
    main()
