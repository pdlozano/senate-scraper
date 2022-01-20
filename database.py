""" # Schema
> All variable types are string

1. `title`: Gives the title of the page. Example:
    "18th Congress - Senate Bill No. 2442 -
    Senate of the Philippines"
2. `name`: Gives the short name of the bill.
    Example: "RIGHT TO REPAIR ACT"
3. `long_name`: Gives the full name of the bill.
    Example: "AN ACT PROMOTING THE RIGHT TO REPAIR
    DIGITAL ELECTRONIC PRODUCTS, AND APPROPRIATING
    FUNDS THEREFOR"
4. `pdf`: Gives a link to the pdf. Example:
    "http://legacy.senate.gov.ph/lisdata/3660132957!.pdf"
5. `scope`: Gives the scope of the bill. Example:
    "National"
6. `author`: Gives the full name of the bill's
    author. Example: "Revilla Jr., Ramon Bong"
"""

import sqlite3
from bill import Bill
from typing import List


class Database:
    def __init__(self):
        self.__db = sqlite3.connect("data.sqlite")

    def insert_item(self, item: Bill) -> bool:
        cur = self.__db.cursor()
        cur.execute("""
            INSERT INTO bills(title, name, long_name, pdf, scope, author)
            VALUES (
                :title,
                :name,
                :long_name,
                :pdf,
                :scope,
                :author
            )
        """, item.to_dict())
        return True
    
    def insert_items(self, items: List[Bill]) -> bool:
        cur = self.__db.cursor()
        cur.executemany("""
            INSERT INTO bills(title, name, long_name, pdf, scope, author)
            VALUES (
                :title,
                :name,
                :long_name,
                :pdf,
                :scope,
                :author
            )
        """, [item.to_dict() for item in items])
        return True
    
    def see_vals(self):
        return self.__db.execute("""
            SELECT * FROM bills;
        """).fetchall()
    
    def close(self):
        self.__db.commit()
        self.__db.close()


if __name__ == "__main__":
    database = sqlite3.connect("data.sqlite")
    database.execute("""
        CREATE TABLE bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            name TEXT NOT NULL,
            long_name TEXT NOT NULL,
            pdf TEXT NOT NULL,
            scope TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
