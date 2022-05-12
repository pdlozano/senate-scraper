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

        find = re.compile(r"Filed on (.+) by (?P<name>.+)")
        author = soup.find(string=find).text.strip()
        author = find.search(author).group("name")
        self.author = get_author_ids(author)

        find = re.compile(r"(?P<stage>(?:First|Second|Third)) Reading")
        reading = soup.find_all(string=find)
        reading = reading[-1].text.strip()
        self.reading = find.search(reading).group("stage")

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
            "reading": self.reading,
        }

    def to_author(self):
        return [
            {
                "authors_id": author,
                "bills_id": self.id,
            }
            for author in self.author
        ]
