from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome(options=chrome_options,executable_path='/usr/local/bin/chromedriver')


driver.get("http://172.24.217.55:3000/d/LQWCv3aMz/chamados")

el = driver.find_element_by_name('user')
el.clear()
el.send_keys("XXXXXXX")

el = driver.find_element_by_name('password')
el.clear()
el.send_keys("XXXXXX")
el.send_keys(Keys.RETURN)


sleep(10)

driver.set_window_size(1920, 3000)

el = driver.find_element_by_tag_name('body')
el.screenshot('/Users/pedroferreira/Downloads/4biz/img.png')
driver.quit()
