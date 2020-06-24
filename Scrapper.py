import csv
import requests
from bs4 import BeautifulSoup as bs

url = requests.get('https://www.lme.com/')

soup = bs(url.content, 'html.parser')

filename = 'test.csv'

csv_writer = csv.writer (open(filename, 'w'))

heading = soup.find('h2')
# table = soup.find_all("table")

for tr in soup.find_all('tr'):
    data =[]
    for th in tr.find_all('th'):
        data.append(th.text)

    if data:
        print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        
    for td in tr.find_all('td'):
        data.append(td.text)
    if data:
        print("Inserting Table Data: {}".format(','.join(data)))
        csv_writer.writerow(data)

