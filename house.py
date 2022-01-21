import requests
from bs4 import BeautifulSoup
from house_bills import HouseMember

url = "https://congress.gov.ph/members/"

if __name__ == "__main__":
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    soup = soup.select("tr.info ~ tr")
    data = HouseMember(soup[0])
