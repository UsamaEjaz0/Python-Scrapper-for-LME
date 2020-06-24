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