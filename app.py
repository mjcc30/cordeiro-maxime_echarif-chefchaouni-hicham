from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import sys
import time
import json
import pandas as pd


if len(sys.argv) == 1:
    print("Veuillez entrez un code postal (ex: 91300)") 
    exit(0)
else:
    print(f"Recherche avec le code postal suivant: {sys.argv[1]}") 

### BDD ###
# Import du package sqlalchemy permetant de gérer les bases de données
import sqlalchemy as db

# Import de la class DataBase permettant de créer des bases de données
from utiles import DataBase

# Instaciation de la base de données 'tenup.sqlite'
database_name = "tenup"
table_name = "tournois"
base = DataBase(database_name)

# Création d'une table nommée "tournois" dans la base de données 'tenup.sqlite'
base.create_table(table_name, 
                 name=db.String, # nom du tournois
                 location=db.String, # - la localisation du tournois
                 start_date=db.String, # date de début        
                 end_date=db.String, # date de fin
                 category=db.String, # catégorie des participants
                 distance=db.String, # la disctance par rapport au point de recherche
                 search_location=db.String, # adresse de la recherche
                 search_time=db.String # la date et l'heure de la recherche
                 )
###

BASE_URL = "https://tenup.fft.fr/recherche/tournois"

search_postal_code =  f"{sys.argv[1]}"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(BASE_URL)
driver.maximize_window()
driver.implicitly_wait(5)

button_cookies = driver.find_element(By.ID, "popin_tc_privacy_button")
button_cookies.click()

input_search = driver.find_element(By.XPATH, '//input[@id="autocomplete-custom-input"]')
input_search.click()

input_search.send_keys(search_postal_code)
time.sleep(2)
input_search.send_keys(Keys.ENTER)
time.sleep(2)
button_search=driver.find_element(By.XPATH, '//*[@id="edit-submit"]')
button_search.click()
search_location = driver.find_element(By.XPATH,'//div[@id="edit-ville"]//div//span/div[@class="reference-autocomplete"]').text
print("search_location", search_location)
time.sleep(2)
tournois = driver.find_elements(By.XPATH,'//div[@class="tournois-results-container"]//li/div[contains(@class,"result-tournament")]')
print('tournois',tournois)
page = int(driver.find_element(By.XPATH,'//*[@id="recherche-tournois-pagination"]/div/ul/li[10]/a').get_attribute('HREF').split("page=")[1])
print('nombre de page:', page)

list_item = []
for j in range(page):
    for i in range(len(tournois)):
        # Création d'un objet item contenant les données à stocker dans la base de données
        item = {}
        print('current page:',j)
        item['name']  = tournois[i].find_element(By.CLASS_NAME,'result-tournament-name').text
        item['location'] = tournois[i].find_element(By.CLASS_NAME,'result-tournament-address').text.split('\n')[0]
        item['distance'] = tournois[i].find_element(By.CLASS_NAME,'result-tournament-address').text.split('\n')[1]
        item['start_date'] = "/".join(tournois[i].find_element(By.CLASS_NAME,'result-tournament-date').text.split(" ")[:3]).replace('.', '')
        item['end_date'] = "/".join(tournois[i].find_element(By.CLASS_NAME,'result-tournament-date').text.split(" ")[3:]).replace('.', '')
        item['category'] = tournois[i].find_element(By.CLASS_NAME,'result-tournament-button').text
        item['search_location'] = search_location
        item['search_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('item:',[(k,v) for k,v in item.items()])
        item_csv_list = [v for _,v in item.items()]
        list_item += [item]
        # Ajout d'une ligne dans la base de données 'tenup.sqlite'
        base.add_row(table_name,
                        name=item['name'], # nom du tournois
                        location=item['location'], # - la localisation du tournois
                        start_date=item['start_date'], # date de début        
                        end_date=item['end_date'], # date de fin
                        category=item['category'], # catégorie des participants
                        distance=item['distance'], # la disctance par rapport au point de recherche
                        search_location=item['search_location'], # le point de recherche
                        search_time=item['search_time'] # la date et l'heure de la recherche
                    )

    next_page = tournois[i].find_element(By.XPATH,'//*[@id="recherche-tournois-pagination"]/div/ul/li[@class="active"]/following-sibling::li/a')
    next_page.click()
    time.sleep(2)

        # //*[@id="recherche-tournois-pagination"]/div/ul/li[9]/a

# Afficher les colonnes de la table
data_read = base.read_table(table_name)
print('table:', data_read)
print('',data_read.columns.keys())

# Afficher le contenu de la table
print(base.select_table(table_name))

# Ajout de la liste dans le fichier 'tenup.json'
with open('tenup.json', 'a') as f:
    json.dump(list_item, f)

# Ajout de la liste dans le fichier 'tenup.csv'
df = pd.DataFrame.from_dict(list_item)
df.to_csv(r'tenup.csv', index = False, header=True)