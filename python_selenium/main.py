from selenium import webdriver
import os
import configparser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

config = configparser.ConfigParser()
config.read("/app/config.ini")

user = config.get('chamados', 'user')
password = config.get('chamados', 'password')
url = config.get('chamados', 'url')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
prefs = {'download.default_directory' : '/app'}
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/sbin/chromedriver')

driver.get(url)
search_bar = driver.find_element_by_name("user_login")
search_bar.clear()
search_bar.send_keys(user)

search_bar = driver.find_element_by_name("senha")
search_bar.clear()
search_bar.send_keys(password)
search_bar.send_keys(Keys.RETURN)

sleep(10)

element = driver.find_element_by_xpath('//*[@id="dataInicio"]')
element.send_keys("01/06/2020")
element = driver.find_element_by_xpath('//*[@id="dataFim"]')
element.send_keys("01/06/2021")


element = driver.find_element_by_xpath('//*[@id="idGrupoAtual"]')
element.send_keys("BR - Unix")
element.send_keys(Keys.RETURN)


element = driver.find_element_by_xpath('//*[@id="btnPesquisar"]')
element.click()
sleep(10)


element = driver.find_element_by_xpath('//*[@id="btnExportCSV"]')
element.click()
sleep(10)
print(driver.title)
driver.quit()
