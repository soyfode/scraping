from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
import random
import json

opts =Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

driver = webdriver.Chrome('../chorome_driver/chromedriver.exe',chrome_options=opts)

# URL SEMILLA
driver.get('https://www.emol.com/nacional')
sleep(random.uniform(2.0, 3.0))

while True:
    nacional = driver.find_elements('xpath','//div[@id="listNews"]/div/h3/a')
    fecha = driver.find_elements('xpath','//div[@id="listNews"]/div/span/span')
    #loop nacional and fecha
    for n,f in zip(nacional,fecha):
        noticia = n.text
        fecha = f.text
        #noticia = p.find_element('xpath','./div/h3/a').text
        #fecha = p.find_element('xpath','./div/span/span').text
        # aggregate data into a dictionary and save to json file
        data = {'titular': noticia, 'fecha': fecha}
        with open('../data/prueba.json', 'a') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write(',\n')
        print(noticia)
        print(fecha)
    sleep(random.uniform(2.0, 3.0))
    try:
        boton=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="li_next"]/a'))
                )
        boton.click()
        WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="listNews"]/div/div[1]/a/img'))
            )
    except:
        break

