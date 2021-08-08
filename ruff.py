import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?'

r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

driver = webdriver.Chrome()

driver.get(url)

html = driver.execute_script('return document.documentElement.outerHTML')

sel_soup = BeautifulSoup(html,'html.parser')

table = sel_soup.find_all('tbody')

table = table[0]

Data = []

for rows in table.find_all('tr'):
    for columns in rows.find_all('td'):
        Data.append(columns.text)

print(Data)

countries = ['USA','Brazil','India','Russia','Peru','Chile','Mexico','South Africa','Pakistan']

for items in range(len(Data)-1):
    if Data[items] in countries:
        countryName = Data[items]
        totalCases = Data[items+1]
        Recovered = Data[items+5]
        Deaths = Data[items+3]
        print(countryName,totalCases,Recovered,Deaths)