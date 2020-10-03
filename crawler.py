import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def crawl(url, data_file):
    options = Options()
    options.headless = True
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)

    driver.get(url)
    sleep(2)

    category = driver.find_element_by_xpath('//h3[1 and text()=\'확진자 추세\']').find_element_by_xpath('..')
    elements = category.find_elements_by_class_name('ZMv3u')
    # print('Length: ' + str(len(elements)))

    value_dic = {}
    for cur in elements:
        action = ActionChains(driver)
        action.move_to_element(cur).perform()
        val_time_origin = driver.find_element_by_class_name('ke9kZe-Rgw69b-bN97Pc')\
            .find_element_by_tag_name('div').find_element_by_tag_name('strong').text
        val_count = int(driver.find_element_by_class_name('TfIRAe').text[8:].replace(',', ''))

        time_split = val_time_origin.replace(' ', '').split('.')
        val_time = (time_split[0][2:]) + (time_split[1].zfill(2)) + (time_split[2].zfill(2))

        print('<' + val_time + '> ' + str(val_count))
        value_dic[val_time] = val_count

    # print(len(value_dic))

    with open(data_file, 'w') as file:
        json_val = json.dumps(value_dic)
        file.write(json_val)

    driver.quit()
