import datetime

from tkinter import Image
from tracemalloc import start
from matplotlib import image
from numpy import empty
import requests, lxml
from bs4 import BeautifulSoup
import urllib.request
import gspread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC






user_agent =  {''}  #INSERT USER AGENT HERE

def render_page(url):
    driver = webdriver.Chrome() #executable_path=fr'C:\Users\Owner\Downloads\chromedriver_win32'
    driver.get(url)
    WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[4]/div/div[1]/div[4]'))).click()
    time.sleep(3)

    r = driver.page_source
    #driver.quit()
    return r

def render_page2(url2):
    driver2 = webdriver.Chrome() #executable_path=fr'C:\Users\Owner\Downloads\chromedriver_win32'
    driver2.get(url2)
    time.sleep(3)
    r2 = driver2.page_source
    #driver.quit()
    return r2


uni = 'https://info.uniswap.org/#/pools'
uni2 ='https://info.uniswap.org/#/'

r2 = render_page2(uni2)
soup2 = BeautifulSoup(r2, 'html.parser')
totalvol = soup2.select('.bRqZpA')[1].text

r = render_page(uni)
soup = BeautifulSoup(r, 'html.parser')
print(soup.prettify())

coinz = []
volumez = []
def scrape():
    for result in soup.select('.dSQPJH', limit=5): #change limit to grab more results I only wanted top 5 trading pairs...
            date = datetime.datetime.now()
            title = result.select_one('.eJnjNO').text
            volume24 = result.select('.eOIWzG')[1].text
            #values = {'date':date, 'title':title, 'volume24':volume24} 
            coinz.append(title)
            volumez.append(volume24)


            print(f'{title}\n{volume24}\n')

scrape()
date = datetime.datetime.now().date()
tim = datetime.datetime.now().time()


print(coinz)
print(volumez)
empty = str('')

#utilizing gspread library for ez export to Google Sheets.
gc = gspread.service_account(filename='creds.json') # insert google service worker account key here.
sh = gc.open('UniswapTradeTracking').sheet1
sh.append_row([str(date), str(tim), empty, str(totalvol), empty, coinz[0], 
    coinz[1], coinz[2], coinz[3], coinz[4], 
    volumez[0], volumez[1], volumez[2], volumez[3]])

print(totalvol)








