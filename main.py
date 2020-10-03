import requests
from bs4 import BeautifulSoup


def crawl(url, cls, delta, data_loc):
    response = requests.get(url)
    # print(response.status_code)
    with open('htm', 'w') as file:
        file.write(str(response.content))


url = 'https://twpower.github.io/17-with-usage-in-python'
data_loc = '/data.dat'
cls = 'TfIRAe'
crawl(url, cls, 0, data_loc)
