import multiprocessing
import requests
from bs4 import BeautifulSoup
from constants import BASE_URL
from bill import Bill
from database import Database


# Initialize Database
db = Database()


# Get Page
def get_page(page_number: int):
    print(f"Getting page no. {page_number}")
    # Get Page
    url = BASE_URL.format(other=f"leg_sys.aspx?congress=18&type=bill&p={page_number}")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # Get all bills
    items = soup.find("div", class_="alight")
    bills = items.find_all("a")

    bills = [bill["href"] for bill in bills]

    # Save bills to database
    bills = [Bill(bill) for bill in bills]
    db.insert_items(items=bills)


# Get pages (310 pages)
pool = multiprocessing.Pool()
pool.map(get_page, range(1, 20))


# Close the Database
db.close()
