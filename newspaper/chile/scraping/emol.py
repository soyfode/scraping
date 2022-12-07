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
driver.get('https://www.emol.com/buscador/?query=')
sleep(random.uniform(1.0, 2.0))

# CLICK EMOL
driver.find_element('xpath','//*[@id="ulIndex"]/li[1]/label').click()
sleep(random.uniform(1.0,2.0))

# CLICK NACIONAL
driver.find_element('xpath','//*[@id="ulCategory"]/li[1]/label').click()
sleep(random.uniform(2.0,5.0))

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

sleep(random.uniform(1.0, 2.0))

while True:

    nacional = driver.find_elements('xpath','//*[@id="ContenedorLinkNoticia"]')

    sleep(random.uniform(1.7, 2.3))

    for n in nacional:
        attempts = 0
        while attempts < 3:
            try:
                noticia = n.find_element(By.ID,"LinkNoticia").text
                fecha = n.find_element('xpath','.//div/span[1]/span[2]').text
                break
            except:
                sleep(random.uniform(1.0, 2.0))
                boton=WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="li_next"]/a/i'))
                        )
                boton.click()
                sleep(random.uniform(2.0, 3.0))
                boton=WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="li_prev"]/a'))
                        )
                boton.click()
                attempts += 0
                sleep(random.uniform(2.0, 3.0))

        data = {'titular': noticia, 'fecha': fecha}
        with open('../data/emol.json', 'a') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write(',\n')

    scroll_to_bottom(driver)

    try:
        boton=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="li_next"]/a/i'))
                )
        boton.click()
        WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="ImgSitio"]'))
            )
        sleep(random.uniform(1.7, 2.3))
    except:
        break

