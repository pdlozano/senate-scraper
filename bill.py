import re
import requests
from bs4 import BeautifulSoup
from constants import BASE_URL, BASE_URL_PDF


class Bill:
    def __init__(self, url):
        item = BASE_URL.format(other=url)
        res = requests.get(item)
        soup = BeautifulSoup(res.text, "html.parser")

        self.title = soup.title.text.strip()
        self.name = soup.find("div", class_="lis_doctitle").text.strip()
        pdf = soup.find("div", id="lis_download").find("a")["href"].strip()
        self.pdf = BASE_URL_PDF.format(other=pdf)

        blockquotes = soup.find_all("blockquote")

        self.long_name = blockquotes[0].text.strip()
        self.scope = blockquotes[1].text.strip()

        find = re.compile(r"Filed on (.+) by (?P<name>.+)")
        author = soup.find(string=find).text.strip()
        self.author = find.search(author).group("name")

    def __repr__(self):
        return self.name

    def to_dict(self):
        return {
            "title": self.title,
            "name": self.name,
            "long_name": self.long_name,
            "pdf": self.pdf,
            "scope": self.scope,
            "author": self.author,
        }
