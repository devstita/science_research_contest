import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

url = 'https://news.google.com/covid19/map?hl=ko&gl=KR&ceid=KR%3Ako'

driver.get(url)
sleep(2)

category = driver.find_element_by_xpath('//h3[1 and text()=\'확진자 추세\']').find_element_by_xpath('..')
elements = category.find_elements_by_class_name('ZMv3u')
print('Length: ' + str(len(elements)))
e_countries = []

for i in range(1):
    value_dic = {}
    for cur in elements:
        action = ActionChains(driver)
        action.move_to_element(cur).perform()
        val_time = driver.find_element_by_class_name('ke9kZe-Rgw69b-bN97Pc')\
            .find_element_by_tag_name('div').find_element_by_tag_name('strong').text
        val_count = int(driver.find_element_by_class_name('TfIRAe').text[8:])
        print('<' + val_time + '> ' + str(val_count))
        value_dic[val_time] = val_count

    e_countries[i] = value_dic

print(len(e_countries[0]))

with open('data.json') as file:
    json_val = json.dumps(e_countries)
    file.write(json_val)

driver.quit()
