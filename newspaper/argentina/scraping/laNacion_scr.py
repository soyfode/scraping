from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import  Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import json


opts =Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

driver = webdriver.Chrome('../chorome_driver/chromedriver.exe',chrome_options=opts)

driver.get('https://www.lanacion.com.ar/politica')

sleep(random.uniform(1.0, 2.0))

button = driver.find_element("id","notificacion-no")
driver.implicitly_wait(6)
ActionChains(driver).move_to_element(button).click(button).perform()

sleep(random.uniform(1.0, 3.0))

def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        sleep(random.uniform(1.0, 2.0))
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))


for i in range(2381):
    try:
        scroll_to_bottom(driver)
        boton=WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="col-12 --loader"]//button[@class="com-button --secondary"]'))
                )
        boton.click()
        WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//time[@class="com-date --fourxs"]'))
            )
    except:
        break

politica = driver.find_elements('xpath','//article[@class="mod-article"]')

for p in politica:
    noticia = p.find_element('xpath','.//section[@class="mod-description"]/h2/a').text
    fecha = p.find_element('xpath','.//section[@class="mod-description"]/time').text
    # aggregate data into a dictionary and save to json file
    data = {'titular': noticia, 'fecha': fecha}
    with open('../data/laNacion_v1.json', 'a') as f:
        json.dump(data, f, ensure_ascii=False)



