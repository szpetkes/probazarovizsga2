"""""""""
1. A Marvel új web alapú rajongó oldalt készít az X-man képregény adaptációkból.

Itt találod a webes applikáció prototípusát: https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html

Készíts egy Python python applikációt (akár csak egy darab python fileban) ami selenium-ot használ.

Teszteld le, hogy a különböző szűrőfeltételek alapján megfelelő karaktereket mutatja az oldal.

Tehát mondjuk iceman pontosan az original és a factor csapatban van benne és a hellfire illetve a force csapatokban 
nincs benne. 

(Figyelem: ne engedd, hogy az oldal dinamikus működése elvonja a figyelmed a célról! A karaktereket csoporthoz 
tartozását nem feltétlenül a felület változásával tudod ellenőrizni.) 

Al alkalmazás helyesen mutatja a felületen a csoporthoz tartozást. Nincs külön tesztadat leírás ehhez a feladathoz, 
tehát a látottak alapáj kell a tesztadatot összeállítanod. 

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat NEM 
kell OOP-t használnod. Viszont tartalmazzon vizsgálatot a megodásod. Lehetőleg használj az assert 
összehasonlításokat. 
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--disable-gpu')

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html')
time.sleep(.5)

# elements
iceman = driver.find_element(By.XPATH, "//li[@id=\'iceman\']/h2")
original_xmen_team = driver.find_element(By.XPATH, "//label[contains(.,\'Original X-Men\')]")
xforce_team = driver.find_element(By.XPATH, "//label[contains(.,\'X-Force\')]")
xfactor_team = driver.find_element(By.XPATH, "//label[contains(.,\'X-Factor\')]")
hellfire_team = driver.find_element(By.XPATH, "//label[contains(.,\'Hellfire Club\')]")

angel = driver.find_element(By.XPATH, "//li[@id=\'angel\']/h2")
beast = driver.find_element(By.XPATH, "//li[@id=\'beast\']/h2")
cyclops = driver.find_element(By.XPATH, "//li[@id=\'cyclops\']/h2")
jean_grey = driver.find_element(By.XPATH, "//li[@id=\'jean-grey\']/h2")
professor_x = driver.find_element(By.XPATH, "//li[@id=\'professor-x\']/h2")
nightcrawler = driver.find_element(By.XPATH, "//li[@id=\'nightcrawler\']/h2")
psylocke = driver.find_element(By.XPATH, "//li[@id=\'psylocke\']/h2")
rictor = driver.find_element(By.XPATH, "//li[@id=\'rictor\']/h2")
storm = driver.find_element(By.XPATH, "//li[@id=\'storm\']/h2")
sunspot = driver.find_element(By.XPATH, "//li[@id=\'sunspot\']/h2")
wolverine = driver.find_element(By.XPATH, "//li[@id=\'wolverine\']/h2")
quicksilver = driver.find_element(By.XPATH, "//li[@id=\'quicksilver\']/img")
emma_frost = driver.find_element(By.XPATH, "//li[@id=\'angel\']/img")
magneto = driver.find_element(By.XPATH, "//li[@id=\'magneto\']/img")
tithe = driver.find_element(By.XPATH, "//li[@id=\'tithe\']/h2")

# teams
original_xmen_team_list = [angel, beast, cyclops, iceman, jean_grey, professor_x]
xforce_team_list = [angel, cyclops, nightcrawler, psylocke, rictor, storm, sunspot, wolverine]
xfactor_team_list = [angel, beast, cyclops, iceman, jean_grey, quicksilver, rictor]
hellfire_team_list = [angel, emma_frost, magneto, psylocke, storm, sunspot, tithe]

original_xmen_team.click()
time.sleep(.5)
assert iceman.is_displayed()
xfactor_team.click()
assert iceman.is_displayed()
time.sleep(.5)
assert iceman.is_displayed()
hellfire_team.click()
time.sleep(.5)
assert iceman.is_displayed()

#or check the name if exist in the teams after clicking? need names to get