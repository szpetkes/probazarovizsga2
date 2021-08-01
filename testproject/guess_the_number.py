"""""""""
3 Feladat: Guess the number automatizálása

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Guess the number app-ot az 
https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az app funkcionalitását tesztelését.

    Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot. Nem 
    jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot a 
    program 

    Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a 
    saját belső számlálóddal. 

    Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat. Az applikéció -19 vagy 
    255 értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e. 

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat vagy 
assert összehasonlításokat. 
"""" """
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--disable-gpu')

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html')
time.sleep(.5)

# elements
newguess = driver.find_element_by_xpath('/html/body/div/div[2]/input')
guessbutton = driver.find_element_by_xpath("/html/body/div/div[2]/span/button")
guesstext = driver.find_element_by_xpath("/html/body/div/p[5]")
guesstextlower = driver.find_element_by_xpath("/html/body/div/p[3]")
guesstexthigher = driver.find_element_by_xpath("/html/body/div/p[4]")
guessesnumber = driver.find_element_by_xpath("/html/body/div/div[3]/p/span")

# number guess
random_number = random.randint(1, 101)
newguess.send_keys(random_number)
guessbutton.click()

if guesstext == 'Guess higher.' or 'Guess lower.':
    newguess.clear()
    random_number = random.randint(1, 101)
    newguess.send_keys(random_number)
    guessbutton.click()

# TC02
newguess.send_keys(-19)
guessbutton.click()
assert guesstextlower.text == "Guess higher."

newguess.send_keys(255)
guessbutton.click()
assert guesstexthigher.text == "Guess lower."
