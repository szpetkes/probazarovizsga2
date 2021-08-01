""""""""""""""""
5 Feladat: Periodusos rendszer

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Periodusos rendszer app-ot az 
https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html oldalról. 

Feladatod, hogy leteszteld, hogy az alábbi sorrendben jelennek-e meg az elemek a weblapon:

(az alábbi tartalmat írd ki kézzel egy data.txt nevű fileba és onnan olvassa fel a kódod a tesztadatot)

1, Hydrogen
2, Helium
3, Lithium
4, Beryllium
5, Boron
6, Carbon
7, Nitrogen
8, Oxygen
9, Fluorine
10, Neon
11, Sodium
12, Magnesium
13, Aluminium
14, Silicon
15, Phosphorus
16, Sulfur
17, Chlorine
18, Argon
19, Potassium
20, Calcium
21, Scandium
22, Titanium
23, Vanadium
24, Chromium
25, Manganese
26, Iron
27, Cobalt
28, Nickel
29, Copper
30, Zinc
31, Gallium
32, Germanium
33, Arsenic
34, Selenium
35, Bromine
36, Krypton
37, Rubidium
38, Strontium
39, Yttrium
40, Zirconium
41, Niobium
42, Molybdenum
43, Technetium
44, Ruthenium
45, Rhodium
46, Palladium
47, Silver
48, Cadmium
49, Indium
50, Tin
51, Antimony
52, Tellurium
53, Iodine
54, Xenon
55, Caesium
56, Barium
57-71, Lanthanide
72, Hafnium
73, Tantalum
74, Tungsten
75, Rhenium
76, Osmium
77, Iridium
78, Platinum
79, Gold
80, Mercury
81, Thallium
82, Lead
83, Bismuth
84, Polonium
85, Astatine
86, Radon
87, Francium
88, Radium
89-103, Actinide
104, Rutherfodum
105, Dubnium
106, Seaborgium
107, Bohrium
108, Hassium
109, Meitnerium
110, Damstadium
111, Roentgenium
112, Ununbium
113, Ununtrium
114, Ununquadium
115, Ununpentium
115, Ununhexium
115, Ununseptum
115, Ununoctium

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest). Egyszerűen használj elágazásokat vagy assert összehasonlításokat.

"""""""""

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

driver.get('https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html')
time.sleep(.5)

elements = []
elements_of_periodic_table = driver.find_elements_by_xpath('/html/body/div/ul/li/span')
for element in elements_of_periodic_table:
    elements.append(element.text)

elments_name_list = []
with open("data.txt", 'rt') as elements_name:
    for i in elements_name:
        elements_name.append(i)
print(elements_name[:2])

assert elements == elments_name_list
