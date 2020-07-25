from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from info import password,e_mail
import random

path = 'C:\drivers\chromedriver'

driver = webdriver.Chrome(path)

driver.get("https://tinder.com/")

time.sleep(4)

close = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button')
close.click()

login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')))
login.click()

login_google = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button')))
login_google.click()

main_tab = driver.window_handles[0]
driver.switch_to.window(driver.window_handles[1])

email = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email.send_keys(e_mail)
email_next = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
email_next.click()

time.sleep(2)

passw = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
passw.send_keys(password)
pass_next = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
pass_next.click()

# time.sleep(3)

driver.switch_to.window(main_tab)


location = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]')))
location.click()

notif_no = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[2]')))
notif_no.click()


like = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')))

r = random.randint(0,1)
t = random.randint(0,5)
while True:
    try:
        if(r < 0.5):
            time.sleep(t)
            t = random.randint(0,10)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'))).send_keys(Keys.SPACE)
        else:
            time.sleep(t)
            t = random.randint(0,10)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'))).send_keys(Keys.SPACE)
        r = random.randint(0,1)
    except:
        driver.quit()
