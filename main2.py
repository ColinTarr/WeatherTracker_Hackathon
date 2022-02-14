from http.server import executable
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import yagmail
from datetime import datetime

yagmail.register('epicsurvivor69@gmail.com', '700F57Aa1')


def weatherProgram():
    s = Service('C:/Users/tarr_colin/Desktop/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get('https://www.accuweather.com/en/us/struthers/44471/daily-weather-forecast/2213244')
    results = []
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    driver.quit()
    print("ya mother")

    for element in soup.findAll(attrs='daily-forecast-card'):
        name = element.find("span", {"class": "high"})
        if name not in results:
            results.append(name.text)
            del results[5:200]
    emailableResults = ' '.join([str(item) for item in results])
    print(emailableResults)
    
    try:
        yag = yagmail.SMTP(user='epicsurvivor69@gmail.com', password='700F57Aa1')
        yag.send(to='Charles.kohn12@gmail.com', subject=f'Weather Alert @ {current_time}', contents=f"Here's the temperature for the next 5 days: {emailableResults}")
        print("Email sent successfully")
    except:
        print("Error, email was not sent")

weatherProgram()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

