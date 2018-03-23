from selenium import webdriver
from bs4 import BeautifulSoup
import os.path
#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\all_room_ads_output.txt"
file_path = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\individual rooms\\"
room_urls_list = []

with open(file_input) as fi:
    content = fi.readlines()
    content = [x.strip() for x in content]
    for x in content:
        room_urls_list.append(x)

ffprofile = "C:/Users/cjwar/AppData/Roaming/Mozilla/Firefox/Profiles/ntnxat2f.Meetup"
driver = webdriver.Firefox(firefox_profile=ffprofile)
for i,x in enumerate(room_urls_list):
    baseurl = x
    driver.get(baseurl)
    # driver.maximize_window()

    try:
        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'nav-bar')))
    except TimeoutException:
        print("",end="")
    html_doc = driver.page_source
    file_path2 = file_path + str(i) + "_room.html"
    with open (file_path2, 'w',encoding='UTF-8') as fp:
        # fp.write(html_code)
        html_doc.encode('UTF-8', 'ignore')
        fp.write(str(html_doc))


driver.quit()
