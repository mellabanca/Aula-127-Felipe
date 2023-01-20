from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
#from webdriver_manager.chrome import ChromeDriveManager
#from selenium.webdriver.chrome.service import Service

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("F:/OneDrive/Melissa/OneDrive/CodigosByjus/aFelipe/27-20-01/chromedriver.exe")
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get(START_URL)

time.sleep(10)

planets_data = []

#Função para coleta de dados
def scrape():

    for i in range(0,10):
        print(f'Coletando dados da página {i+1} ...' )
        
        # Objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Loop para encontrar o elemento dentro das tags ul e li
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")
           
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)

scrape()
print(planets_data[1])