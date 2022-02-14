from http.server import executable
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import yagmail
from datetime import datetime

yagmail.register('epicsurvivor69@gmail.com', '700F57Aa1')


def weatherProgram():
    driver = webdriver.Chrome(executable_path='C:/Users/tarr_colin/Desktop/chromedriver.exe')
    driver.get('https://www.accuweather.com/en/us/struthers/44471/daily-weather-forecast/2213244')
    results = []
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    driver.quit()

    for element in soup.findAll(attrs='daily-forecast-card'):
        name = element.find("span", {"class": "high"})
        if name not in results:
            results.append(name.text)
            del results[5:200]
    print(results)
    emailableResults = ' '.join([str(item) for item in results])
    print(emailableResults)
    

    try:
        #initializing the server connection
        yag = yagmail.SMTP(user='epicsurvivor69@gmail.com', password='700F57Aa1')
        #sending the email
        yag.send(to='Charles.kohn12@gmail.com', subject=f'Weather Alert @ {current_time}', contents=f"Hey here's the weather tard. {emailableResults}")
        print("Email sent successfully")
    except:
        print("Error, email was not sent")


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

