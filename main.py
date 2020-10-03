import crawler
import json

url = 'https://news.google.com/covid19/map?hl=ko&gl=KR&ceid=KR%3Ako'
data_loc = 'data/worldwide.json'

need_crawl = input('Crawl? ')
if need_crawl.lower() == 'y':
    crawler.crawl(url, data_loc)

with open(data_loc) as file:
    data = json.loads(file.read())
