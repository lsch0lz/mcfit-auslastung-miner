from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from datetime import datetime, date

mystring = "Auslastung "

studio1 = "berlin-lichterfelde"
studio2 = "berlin-marzahn"
studio3 = "berlin-lichtenberg"
studio4 = "berlin-reinickendorf"
studio5 = "berlin-mahlsdorf"
studio6 = "berlin-wilmersdorf"
studio7 = "berlin-spandau-west"
studio8 = "berlin-spandau"

studios = studio1, studio2, studio3, studio4, studio5, studio6, studio7, studio8

def get_auslastung(studio):


        url = "https://www.mcfit.com/de/fitnessstudios/studiosuche/studiodetails/studio/"
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url + studio)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "lxml")

        auslastung = soup.find_all('div', {'class': 'sc-iJCRLp eDJvQP'})
        #print(auslastung)
        #auslastung = str(auslastung).split("<span>")[1]
        #print(auslastung)
        #auslastung = auslastung[:auslastung.rfind('</span>')]
        #print(auslastung)

        auslastung = str(auslastung).split("Auslastung ")[1]
        #print(auslastung)
        auslastung = auslastung[:auslastung.rfind('%')]
        print(auslastung)


        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        today = date.today()

        print(today)
        #print(studio)

        ergebnis = {'date': today, 'time': current_time, 'studio': studio, 'auslastung': auslastung}

        return ergebnis

        driver.close()

import csv

with open('data.csv', mode='a') as file:
    fieldnames = ['date', 'time', 'studio', 'auslastung']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    today_warning = date.today()

    for studio in studios:
        try:
            print(studio)
            writer.writerow(get_auslastung(studio))
        except Exception:
            print("!!!!RETRYING!!!!")
            writer.writerow(get_auslastung(studio))
            #print("Exception: Continue")
            #continue

