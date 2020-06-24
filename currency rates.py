import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.x-rates.com/calculator/?from=GBP&to=USD&amount=1')
soup = BeautifulSoup(page.text, 'html.parser')

part1 = soup.find(class_="ccOutputTrail").previous_sibling
part2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
rate = "{}{}".format(part1,part2)

def gbp_to_usd(rate,gbp):
    dollars=gbp*rate
    return dollars

gbp = input("Enter GBP amount: ")
finalamt = gbp_to_usd(float(rate),float(gbp))
print(str(gbp)+" GBP is equvalent to "+"$"+str(finalamt)+" USD")