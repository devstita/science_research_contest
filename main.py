import crawler
import json

url = 'https://news.google.com/covid19/map?hl=ko&gl=KR&ceid=KR%3Ako'
data_loc = 'data/worldwide.json'

need_crawl = input('Crawl? ')
if need_crawl.lower() == 'y':
    crawler.crawl(url, data_loc)

with open(data_loc) as file:
    data_origin = json.loads(file.read())

data_origin_keys = list(data_origin.keys())
stacked_cases = [data_origin[data_origin_keys[0]]]
idx = 0
for key in data_origin_keys[1:]:
    stacked_cases.append(stacked_cases[idx] + data_origin[key])
    idx += 1
