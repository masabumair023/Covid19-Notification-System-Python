from plyer import notification
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def NotifyMe(title, message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "D:\PYTHON\Projects\COVID-19 NOTIFICATION SYSTEM\icon (1).ico",
    timeout = 30
     )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    
    url = 'https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?'

    r = requests.get(url)

    soup = BeautifulSoup(r.content,'html.parser')

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)


    # driver = webdriver.Chrome('D:\\PYTHON\\Projects\\COVID-19 NOTIFICATION SYSTEM\\chromedriver.exe')

    driver.get(url)

    html = driver.execute_script('return document.documentElement.outerHTML')

    sel_soup = BeautifulSoup(html,'html.parser')

    table = sel_soup.find_all('tbody')

    table = table[0]

    Data = []

    for rows in table.find_all('tr'):
        for columns in rows.find_all('td'):
            Data.append(columns.text)

    countries = ['USA','Brazil','India','Pakistan','Italy','Saudi Arabia']

    for items in range(len(Data)-1):
        if Data[items] in countries:
            countryName = Data[items]
            totalCases = Data[items+1]
            Recovered = Data[items+5]
            Deaths = Data[items+3]
            nTitle = 'Cases of COVID-19'
            nText = f"Country: {countryName}\n Total Cases: {totalCases}\n Recovered: {Recovered}\n Deaths: {Deaths}"
            NotifyMe(nTitle,nText)
            time.sleep(5) 