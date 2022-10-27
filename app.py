from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://tenup.fft.fr/recherche/tournois"


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get(BASE_URL)
driver.maximize_window()

button_cookies = driver.find_element(By.ID, "popin_tc_privacy_button")
button_cookies.click()

input_search = driver.find_element(By.XPATH, '//input[@id="autocomplete-custom-input"]')
input_search.click()
input_search.send_keys("Massy, 91, Essonne, Île-de-France")
input_search.send_keys(Keys.ENTER)

button_search=driver.find_element(By.XPATH, '//*[@id="edit-submit"]')
button_search.click()

tournois = driver.find_elements(By.TAG_NAME,'li')


for tournoi in tournois:
    nom = tournoi.find_element(By.XPATH,'//*[@id="block-system-main"]/div/div[2]/ul/li[1]/div/div[1]/a/div[1]').text
    localisation = tournoi.find_element(By.XPATH,'//*[@id="block-system-main"]/div/div[2]/ul/li[1]/div/div[1]/a/div[2]').text.split('\n')[0]
    distance = tournoi.find_element(By.XPATH,'//*[@id="block-system-main"]/div/div[2]/ul/li[1]/div/div[1]/a/div[2]').text.split('\n')[1]
       





