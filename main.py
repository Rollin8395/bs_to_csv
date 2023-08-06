from bs4 import BeautifulSoup
import requests
import time
def find_interns():
    html_text=requests.get('https://internshala.com/internships/software-development-internship/').text
    #with open('2355 Work From Home Internships _ Online Internships.html','r') as html_file:
    #html_text=html_file.read()
    soup=BeautifulSoup(html_text,'lxml')
    interns=soup.find_all('div',class_='internship_meta')
    for index, intern in enumerate(interns):
        published_time=intern.find('div',class_='status-container').text
        #print(published_time)
        if 'Few' in published_time:
            company_name=intern.find('div',class_='company_and_premium').text.replace(' ','')
            link=intern.find('a',class_='view_detail_button')['href']
            Stipned=intern.find('div',class_='other_detail_item stipend_container')
            for Stip in Stipned:
                Stip=Stipned.find('div',class_='item_body').text
                with open(f'posts/{index}.txt','w',encoding='utf-8') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Details: {link.strip()} \n')
                    f.write(f'Stipned:{Stip}')
                print(f'File Saved:{index}')


if __name__=='__main__':
    while True:
        find_interns()
        time_wait=10
        time.sleep(time_wait)
        print(f"Waitintg for {time_wait} seconds...")