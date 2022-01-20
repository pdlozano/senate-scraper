import re
import requests
from bs4 import BeautifulSoup
from constants import BASE_URL, BASE_URL_PDF
from authors import get_author_ids


class Bill:
    def __init__(self, url: str):
        item = BASE_URL.format(other=url)
        res = requests.get(item)
        soup = BeautifulSoup(res.text, "html.parser")
        res = requests.post(item, data={
            "__EVENTTARGET": "lbAll",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": soup.find(id="__VIEWSTATE")['value'],
            "__VIEWSTATEGENERATOR": soup.find(id="__VIEWSTATEGENERATOR")['value'],
            "__EVENTVALIDATION": soup.find(id="__EVENTVALIDATION")['value'],
        })
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.title.text.strip()
        title = re.search(
            r".+ Congress - (?P<title>.+) - Senate of the Philippines", title
        )
        self.title = title.group("title")
        self.name = soup.find("div", class_="lis_doctitle").text.strip()
        pdf = soup.find("div", id="lis_download").find("a")["href"].strip()
        self.pdf = BASE_URL_PDF.format(other=pdf)

        blockquotes = soup.find_all("blockquote")

        self.long_name = blockquotes[0].text.strip()
        self.scope = blockquotes[1].text.strip()
        self.primary_committee = blockquotes[4].text.strip()
        self.secondary_commitee = blockquotes[5].text.strip()

        try:
            find = re.compile(r"Introduced by Senators? (?P<name>.+);")
            # http://legacy.senate.gov.ph/lis/bill_res.aspx?congress=18&q=SBN-2419
            # http://legacy.senate.gov.ph/lis/bill_res.aspx?congress=18&q=SBN-2439
            # http://legacy.senate.gov.ph/lis/bill_res.aspx?congress=18&q=SBN-2409
            introduced_by = soup.find(string=find).text.strip()
            introduced_by = find.search(introduced_by).group("name")
            self.introduced_by = get_author_ids(introduced_by)
        except AttributeError:
            try:
                sponsor = blockquotes[7].text.strip()
                self.introduced_by = get_author_ids(sponsor)
            except IndexError:
                self.introduced_by = []
                print(item)

        find = re.compile(r"Filed on (.+) by (?P<name>.+)")
        author = soup.find(string=find).text.strip()
        author = find.search(author).group("name")
        self.author = get_author_ids(author)

        self.id = hash(self.title)

    def __repr__(self):
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "name": self.name,
            "long_name": self.long_name,
            "pdf": self.pdf,
            "scope": self.scope,
        }

    def to_author(self):
        return [
            {
                "authors_id": author,
                "bills_id": self.id,
            }
            for author in self.author
        ]

    def to_sponsor(self):
        return [
            {
                "sponsor_id": sponsor,
                "bills_id": self.id,
            }
            for sponsor in self.introduced_by
        ]
