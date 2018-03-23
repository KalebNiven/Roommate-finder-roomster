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

file_path = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\"



baseurl = "https://www.roomster.com/haveshare/Dallas,%20TX,%20USA/"
# username = "admin"
# password = "admin"
#
# xpaths = { 'usernameTxtBox' : "//input[@name='username']",
#            'passwordTxtBox' : "//input[@name='password']",
#            'submitButton' :   "//input[@name='login']"
#          }


ffprofile = "C:/Users/cjwar/AppData/Roaming/Mozilla/Firefox/Profiles/ntnxat2f.Meetup"
driver = webdriver.Firefox(firefox_profile=ffprofile)
driver.get(baseurl)
# driver.maximize_window()

try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'nav-bar')))
except TimeoutException:
    print("",end="")
# url = "https://classroom.udacity.com/courses/cs253"
# driver.get(url)
# time.sleep(1)

filter = driver.find_elements_by_class_name("filer")#[0].click()
filter[0].click()

sex_male = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div[1]/div/div[3]/div/div[3]/div[2]/div[2]")#[0].click()
sex_male.click()


driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div[1]/div/div[3]/div/div[6]/div[2]/button[1]").click() #click the apply filter button
# driver.ExecuteScript('"'document.getElementsByClassName("budgetValue").innerHTML = "950";'"')
# print(len(number_of_jobs))
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    html_doc = driver.page_source
    file_path2 = file_path + str(i) + "_room_list.html"
    with open (file_path2, 'w',encoding='UTF-8') as fp:
        # fp.write(html_code)
        html_doc.encode('UTF-8', 'ignore')
        fp.write(str(html_doc))
# for i in range()


# print(html_doc)

driver.quit()
