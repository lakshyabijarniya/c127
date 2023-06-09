import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

def scrape():
    headers = ["names", "light_years", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            
            temp_list=[]
            
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                    
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                        
                    except:
                        temp_list.append("")
                        
            planet_data.append(temp_list)
            
        browser.find_element('xpath','//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open("scaper2.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)
        

scrape()