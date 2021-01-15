from selenium import webdriver
import os
import configparser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
prefs = {'download.default_directory' : '/app'}
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/sbin/chromedriver')

# SCREENSHOT
driver.get("http://191.252.182.151:3000/d/LQWCv3aMz/chamados")

el = driver.find_element_by_name('user')
el.clear()
el.send_keys("XXXXXXXX")

el = driver.find_element_by_name('password')
el.clear()
el.send_keys("XXXXXXX")
el.send_keys(Keys.RETURN)

sleep(600)


driver.set_window_size(1920, 3000)

el = driver.find_element_by_tag_name('body')
el.screenshot('/app/img.png')
driver.quit()
