import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import openpyxl
import csv


def get_data():
    #html_text=requests.get('https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4').text
    driver = webdriver.Chrome()
    url = "https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4"
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    soup=BeautifulSoup(page_source,'lxml')
    Details=[]
    Values=[]
    ETH_price=soup.find('span',class_='text-muted').get_text()
    ETH_value=soup.find('a').get_text()
    TH=soup.find('div',class_='col-md-3 text-dt mb-2 mb-md-0').get_text().strip()
    TH_value=soup.find('span',class_='me-1').get_text()
    Status=soup.find('div',class_='col-auto col-md-3 text-dt mb-1 mb-md-0').get_text()
    Status_v=soup.find('span',class_='badge bg-success bg-opacity-10 border border-success border-opacity-25 text-green-600 fw-medium text-start text-wrap py-1.5 px-2').get_text()
    b= soup.find('div', class_='col-md-3 text-dt mb-2 mb-md-0').get_text()
    block_v=soup.find('span',class_='d-flex align-items-center gap-1').get_text()
    TA=soup.find('div',class_='col-md-3 text-dt mb-1 mb-md-0').get_text()
    TA_value=soup.find('div',class_='d-flex align-items-baseline').get_text()
    From_v=soup.find('div',class_='col-md-9').get_text()


    print()
    Detail=[ETH_price,TH,Status,b,TA,'From']
    Value=[ETH_value,TH_value,Status_v,block_v,TA_value,From_v]
    Details.extend(Detail)
    Values.extend(Value)

    return Details,Values




def CSV(details,values):
    filename = "New.csv"

    with open(filename, "w", encoding="utf-8") as f:
        f.write = csv.writer(f)
        f.write.writerow(['Number', 'Detail', 'Value'])
        for i in range(len(values)):
            f.write.writerow([i + 1, details[i], values[i]])

if __name__=='__main__':
    data,value=get_data()
    CSV(data,value)
