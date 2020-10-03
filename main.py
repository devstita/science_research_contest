import crawler
from visualizer import visualize
import json
import ml_core

url = 'https://news.google.com/covid19/map?hl=ko&gl=KR&ceid=KR%3Ako'
data_loc = 'data/worldwide.json'

need_crawl = input('Crawl? ')
if need_crawl.lower() == 'y':
    crawler.crawl(url, data_loc)

with open(data_loc) as file:
    data_origin = json.loads(file.read())

data_origin_keys = list(data_origin.keys())
start_date = data_origin_keys[0]
print(start_date)

stacked_cases = [data_origin[data_origin_keys[0]]]
idx = 0
for key in data_origin_keys[1:]:
    stacked_cases.append(stacked_cases[idx] + data_origin[key])
    idx += 1

x_train = []
y_train = []
for (i, cur) in enumerate(stacked_cases):
    x_train.append(i)
    y_train.append(cur)

ml_core.train(x_train, y_train)
query_x_data = []
query_y_data = []
for i in range(1000):
    (x, y) = (i, ml_core.query([i]))
    print('(' + str(x) + ', ' + str(y) + ')')
    query_x_data.append(i)
    query_y_data.append(ml_core.query([i]))
visualize(query_x_data, 'X', query_y_data, 'Y')
