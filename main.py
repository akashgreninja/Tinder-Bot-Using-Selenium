

#readme 

#PLEASE DO NOT CHANGE THE SLEEP TIME IT WILL MESS UP THE CODE
#DO NOT CLICK IN BETWEEN THE PROCESSES 
#CHANGE ONLY THE EMAIL ON LINE 32
#CHANGE ONLY THE EMAIL ON LINE 33
#CHANGE ONLY THE EMAIL ON LINE 34







import time

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

Email="Your FB ID"
Password="Your FB password"
SWIPES="ENTER THE AMOUNT OF SWIPES KEEP IT <100"


driver.get("https://tinder.com/")
time.sleep(2)
create_account = driver.find_element(By.XPATH,'//*[@id="q1028785088"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
create_account.click()
time.sleep(2)



# facebook_login.click()


try:
    facebook_login=driver.find_element(By.XPATH,'//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/button')
    qt=driver.find_element(By.XPATH,'//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
    qt.click()
    # selection_facebook=driver.find_elements(By.CSS_SELECTOR,'button')
    # for i in selection_facebook:
    #     print(i.text)
    # selection_facebook[8].click()



except NoSuchElementException:

    time.sleep(4)
    find_elements=driver.find_element(By.XPATH,'//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/button')
    find_elements.click()
    time.sleep(3)
    fb_click=driver.find_element(By.XPATH,'//*[@id="q-699595988"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
    fb_click.click()
    print("wanda")




#to nav between windows
print(driver.window_handles)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


time.sleep(5)
facebook_login_session_email=driver.find_element(By.XPATH,'//*[@id="email"]')
facebook_login_session_email.send_keys(Email)
facebook_login_session_password=driver.find_element(By.XPATH,'//*[@id="pass"]')
facebook_login_session_password.send_keys(Password)

facebook_login_session_password.send_keys(Keys.ENTER)
time.sleep(2)

driver.switch_to.window(base_window)
print("base")

time.sleep(7)
location=driver.find_element(By.XPATH,'//*[@id="q-699595988"]/div/div/div/div/div[3]/button[1]')
location.click()

disable=driver.find_element(By.XPATH,'//*[@id="q-699595988"]/div/div/div/div/div[3]/button[2]')
disable.click()


time.sleep(6)

for i in range(SWIPES):
    time.sleep(1)
    try:

        body = driver.find_element(By.CSS_SELECTOR,'body')
        body.send_keys(Keys.RIGHT)


    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        
        except NoSuchElementException:
            time.sleep(2)




