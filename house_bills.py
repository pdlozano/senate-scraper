import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class HouseMember:
    def __init__(self, info: Tag):
        url = info.find("a")['href'].strip()[2:]
        url = "https://congress.gov.ph" + url
        td = info.find_all("td")
        self.name = td[0].find("a").text.strip()
        self.representative = td[1].text.strip()

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        panel = soup.find(class_="panel-default")
        self.headings = panel.find_all(class_="panel-heading")
        self.body = panel.find_all(class_="panel-body")


class HouseBill:
    def __init__(self, heading, body):
        self.id = hash(self.title)
        self.title = heading.text.strip()
        self.scope = ""
        self.full_name = ""
