from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
driver = webdriver.Firefox()

def GameStarter():
    driver.get(F'https://igo.gamestarter.com/#igo')

def GameFi():
    driver.get('https://hub.gamefi.org/#/pools/token')
    classes = driver.find_elements_by_class_name("jss13")
    for element in classes:
        title = driver.find_element_by_css_selector("div.MuiBox-root:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(1)")
        print(title)
        """file1 = open("export.txt","w")
        L = [title]
        file1.write(L)
        file1.close()"""

GameFi()
