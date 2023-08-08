from selenium import webdriver
from bs4 import BeautifulSoup
import time
import openpyxl
import pandas as pd
import csv


def get_data():
    #html_text=requests.get('https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4').text
    driver = webdriver.Chrome()
    url = "https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4"
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    soup=BeautifulSoup(page_source,'lxml')
    datas=soup.find_all('div',class_='row mb-4')
    print(datas)


    for data in datas:
       Details=data.find('div',class_='col-md-3 text-dt mb-2 mb-md-0').text()
       print(Details)




if __name__=='__main__':
    get_data()