"""""""""
2. Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a sales Film register app-ot az 
https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html oldalról. 

Feladatod, hogy automatizáld az alkalmazás két funkciójának a tesztelését

Teszteld le, hogy betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db.
Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet:
        Film title: Black widow
        Release year: 2021
        Chronological year of events: 2020
        Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
        Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
        Film summary: https://www.imdb.com/title/tt3480822/

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat vagy 
assert összehasonlításokat. ""''"" """

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

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html')
time.sleep(.5)

# TC01
movies = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
assert len(movies) <= 24

# TC02 register new movie
# tesdata
Film_title = 'Black widow'
Release_year = '2021'
Chronological_year_of_events = '2020'
Trailer_url = 'https://www.youtube.com/watch?v=Fp9pNPdNwjI'
Image_url = 'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg'
Film_summary = 'https://www.imdb.com/title/tt3480822/'

# register new movie
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/button").click()
time.sleep(1)
driver.find_element_by_id("nomeFilme").send_keys(Film_title)
driver.find_element_by_id("anoLancamentoFilme").send_keys(Release_year)
driver.find_element_by_id("anoCronologiaFilme").send_keys(Chronological_year_of_events)
driver.find_element_by_id("linkTrailerFilme").send_keys(Trailer_url)
driver.find_element_by_id("linkImagemFilme").send_keys(Image_url)
driver.find_element_by_id("linkImdbFilme").send_keys(Film_summary)

# save movie
driver.find_element(By.XPATH, "//button[@onclick=\'salvarFilme()\']").click()

# assert
movies_list = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
assert len(movies_list) == 25
