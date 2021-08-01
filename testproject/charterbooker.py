"""""""""
4 Feladat: charterbooker automatizálása
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a charterbooker app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html 
oldalról. 
Feladatod, hogy automatizáld selenium webdriverrel a charterbooker app tesztelését.
Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat vagy 
assert összehasonlításokat. 
1. Teszteld le a többoldalas formanyomtatvány működését. Ellenőrizd a helyes kitöltésre adott választ: "Your message 
    was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're 
    sailing or eating tacos!)." 
2. Készíts tesztesetet az e-mail cím validációjára. 
"""" """

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--disable-gpu')

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html')
time.sleep(.5)

# TC01 valid email
date_of_jouney = '2021.08.10'
hours = '3'
name = 'Petkes Szabolcs'
email = 'sz.petkes@gmail.com'
message = 'no thank you'
bookingok = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like " \
            "lightning (Unless we're sailing or eating tacos!). "

driver.find_element(By.XPATH, "//select[@name=\'bf_totalGuests\']").click()
time.sleep(.5)
dropdown = driver.find_element(By.NAME, "bf_totalGuests")
dropdown.find_element(By.XPATH, "//option[. = '1']").click()
driver.find_element(By.XPATH, "//div[@id=\'step1\']/ul/li[2]/button").click()
driver.find_element(By.XPATH, "//input[@name=\'bf_date\']").send_keys(date_of_jouney)
driver.find_element(By.NAME, "bf_time").click()
dropdown = driver.find_element(By.NAME, "bf_time")
dropdown.find_element(By.XPATH, "//option[. = 'Morning']").click()
hoursj = Select(driver.find_element_by_name('bf_hours'))
hoursj.select_by_visible_text(hours)
driver.find_element(By.CSS_SELECTOR, ".next-btn2").click()
driver.find_element(By.XPATH, "//input[@name=\'bf_fullname\']").send_keys(name)
driver.find_element(By.XPATH, "//input[@name=\'bf_fullname\']").click()
driver.find_element(By.XPATH, "//input[@name=\'bf_email\']").send_keys(email)
driver.find_element(By.XPATH, "//input[@name=\'bf_email\']").click()
driver.find_element(By.XPATH, "//textarea[@name=\'bf_message\']").click()
driver.find_element(By.XPATH, "//textarea[@name=\'bf_message\']").send_keys(message)
driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()

assert driver.find_element_by_xpath("//*[@id='booking-form']/h2").text == bookingok

# TC02 non valid email
date_of_jouney = '2021.08.10'
hours = '3'
name = 'Petkes Szabolcs'
email = 'sz.petkes@'
message = 'no thank you'
bookingok = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like " \
            "lightning (Unless we're sailing or eating tacos!). "

driver.find_element(By.XPATH, "//select[@name=\'bf_totalGuests\']").click()
time.sleep(.5)
dropdown = driver.find_element(By.NAME, "bf_totalGuests")
dropdown.find_element(By.XPATH, "//option[. = '1']").click()
driver.find_element(By.XPATH, "//div[@id=\'step1\']/ul/li[2]/button").click()
driver.find_element(By.XPATH, "//input[@name=\'bf_date\']").send_keys(date_of_jouney)
driver.find_element(By.NAME, "bf_time").click()
dropdown = driver.find_element(By.NAME, "bf_time")
dropdown.find_element(By.XPATH, "//option[. = 'Morning']").click()
hoursj = Select(driver.find_element_by_name('bf_hours'))
hoursj.select_by_visible_text(hours)
driver.find_element(By.CSS_SELECTOR, ".next-btn2").click()
driver.find_element(By.XPATH, "//input[@name=\'bf_fullname\']").send_keys(name)
driver.find_element(By.XPATH, "//input[@name=\'bf_fullname\']").click()
driver.find_element(By.XPATH, "//input[@name=\'bf_email\']").send_keys(email)
driver.find_element(By.XPATH, "//input[@name=\'bf_email\']").click()
driver.find_element(By.XPATH, "//textarea[@name=\'bf_message\']").click()
driver.find_element(By.XPATH, "//textarea[@name=\'bf_message\']").send_keys(message)
driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()

assert driver.find_element_by_xpath("//*[@id='booking-form']/h2").text == bookingok
