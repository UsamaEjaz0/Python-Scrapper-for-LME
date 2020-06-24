import csv
import requests
from bs4 import BeautifulSoup as bs

from pandas.io.html import read_html
import lxml

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.x-rates.com/calculator/?from=USD&to=PKR&amount=1')
soup = BeautifulSoup(page.text, 'html.parser')

part1 = soup.find(class_="ccOutputTrail").previous_sibling
part2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
rate = "{}{}".format(part1,part2)

def usd_to_pkr(rate,gbp):
    dollars=gbp*rate
    return dollars

gbp = input("Enter USD amount: ")
finalamt = usd_to_pkr(float(rate),float(gbp))
print(str(gbp)+" USD is equvalent to "+str(finalamt)+" PKR")
# url = "https://www.lme.com/"
#
#
# page = requests.get(url)
#
# tables = read_html(page.text, attrs={"class":"ring-times"})
# print(tables[0].head())
# tables[0].to_excel("df.xlsx")

url = "https://www.lme.com/en-GB/Metals/Non-ferrous#tabIndex=0"

page = requests.get(url)

tables = read_html(page.text)
print(tables[0].head())
tables[0].to_excel("df.xlsx")
#
# soup = bs(url.content, 'html.parser')
#
# filename = 'test.csv'
#
# csv_writer = csv.writer (open(filename, 'w'))
#
# heading = soup.find('h2')
# # table = soup.find_all("table")
#
# for tr in soup.find_all('tr'):
#     data = []
#     for th in tr.find_all('th'):
#         data.append(th.text)
#
#     if data:
#         print("Inserting headers : {}".format(','.join(data)))
#         csv_writer.writerow(data)
#         continue
#     for td in tr.find_all('td'):
#         print(td.text)
#     if data:
#         print("Inserting Table Data: {}".format(','.join(data)))
#
#         csv_writer.writerow(data)
#
