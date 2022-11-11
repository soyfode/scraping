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

driver.maximize_window()

# URL SEMILLA
driver.get('https://www.lanacion.com.ar/buscador/?query=la%20')
sleep(random.uniform(1.0, 2.0))

button = driver.find_element("id","notificacion-no")
driver.implicitly_wait(6)
ActionChains(driver).move_to_element(button).click(button).perform()
sleep(random.uniform(1.0,2.0))

driver.find_element('xpath','//*[@id="section_filter"]/div[3]/a').click()
sleep(random.uniform(1.0,2.0))

# CAMBIO DE SECCIONES "NUEVO"
select = Select(driver.find_element('xpath','//select[@id="sortby"]'))
select.select_by_visible_text('NUEVO')
sleep(random.uniform(1.0, 2.0))

# FECHA INICIO
fechaInicio = driver.find_element("xpath",'//*[@id="datepicker_from"]')
fechaInicio.send_keys('01/01/2013')
sleep(random.uniform(1.0, 2.0))

# FECHA FINAL
fechaFinal = driver.find_element("xpath",'//*[@id="datepicker_to"]')
fechaFinal.send_keys('31/12/2014')
sleep(random.uniform(1.0, 2.0))
fechaFinal.send_keys(Keys.ESCAPE)
sleep(random.uniform(1.0, 2.0))

# ACEPTAR FECHA
driver.find_element("xpath",'//*[@id="pubDate_filter"]/div[7]/button').click()
sleep(random.uniform(1.0, 2.0))


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

# PARA PÁGINAS HORIZONTALES Y VERTICALES
"""
links = driver.find_elements('xpath','//*[@id="resultdata"]/div/div/a')
while True:
    link_pagina = []
    for tag_a in links:
        link_pagina.append(tag_a.get_attribute('href'))

    for link in link_pagina:
        try:
            driver.get(link)
            titular = driver.find_element('xpath','//*[@id="content"]/div[7]/div/div/h1').text
            fecha = driver.find_element('xpath','//*[@id="content"]/div[8]/div[1]/div/div/span/time[1]').text
            hora = driver.find_element('xpath','//*[@id="content"]/div[8]/div[1]/div/div/span/time[2]').text
            print(titular)
            print(fecha)
            print(hora)
            driver.back()
        except Exception as e:
            print(e)
            driver.back()

    try:
        scroll_to_bottom(driver)
        driver.find_element(By.XPATH,'//a[text(),"Siguiente")]').click()
    except:
        break
"""

while True:
    politica = driver.find_elements('xpath','//*[@id="resultdata"]//div[@class="queryly_item_row"]')
    for p in politica:
        noticia = p.find_element('xpath','./div/a/div').text
        fecha = p.find_element('xpath','./div/div[2]').text
        # aggregate data into a dictionary and save to json file
        data = {'titular': noticia, 'fecha': fecha}
        with open('../data/laNacion2022.json', 'a') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write(',\n')
    scroll_to_bottom(driver)
    try:
        boton=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="resultdata"]//a[@class="next_btn"]'))
                )
        boton.click()
        WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="queryly_advanced_item_imagecontainer"]'))
            )
    except:
        break

