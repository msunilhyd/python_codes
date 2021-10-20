import requests
from bs4 import BeautifulSoup

data = requests.get('https://xossipz.com/Thread-desi-pics-hot-indian-boobs').text
soup = BeautifulSoup(data, 'lxml')

for link in soup.findAll('a', {'class': 'mycode_url'}):
    try:
        print(link['href'] + '#')
    except KeyError:
        pass
