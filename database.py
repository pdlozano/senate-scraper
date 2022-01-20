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
from itertools import chain


class Database:
    def __init__(self):
        self.__db = sqlite3.connect("data.sqlite")
        self.__db.execute(
            """
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                name TEXT NOT NULL,
                long_name TEXT NOT NULL,
                pdf TEXT NOT NULL,
                scope TEXT NOT NULL
            )
        """
        )

        self.__db.execute(
            """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first TEXT NOT NULL,
                last TEXT NOT NULL
            );
        """
        )

        self.__db.execute(
            """
            CREATE TABLE IF NOT EXISTS bills_authors (
                bills_id INTEGER,
                authors_id INTEGER,
                FOREIGN KEY(bills_id) REFERENCES bills(id),
                FOREIGN KEY(authors_id) REFERENCES authors(id)
            );
        """
        )

        self.__db.execute(
            """
            INSERT OR IGNORE INTO authors (id, first, last)
            VALUES  (1, 'Sonny', 'Angara'),
                    (2, 'Maria Lourdes Nancy S.', 'Binay'),
                    (3, 'Pia S.', 'Cayetano'),
                    (4, 'Leila M.', 'De Lima'),
                    (5, 'Ronald "Bato"', 'Dela Rosa'),
                    (6, 'Franklin M.', 'Drilon'),
                    (7, 'Win', 'Gatchalian'),
                    (8, 'Christopher Lawrence T.', 'Go'),
                    (9, 'Richard J.', 'Gordon'),
                    (10, 'Risa', 'Hontiveros'),
                    (11, 'Panfilo "Ping" M.', 'Lacson'),
                    (12, 'Manuel "Lito" M.', 'Lapid'),
                    (13, 'Imee R.', 'Marcos'),
                    (14, 'Emmanuel "Manny" D.', 'Pacquiao'),
                    (15, 'Francis "Kiko" N.', 'Pangilinan'),
                    (16, 'Aquilino "Koko" III', 'Pimentel'),
                    (17, 'Grace', 'Poe'),
                    (18, 'Ralph G.', 'Recto'),
                    (19, 'Ramon Bong', 'Revilla Jr.'),
                    (20, 'Vicente C.', 'Sotto III'),
                    (21, 'Francis "Tol" N.', 'Tolentino'),
                    (22, 'Joel', 'Villanueva'),
                    (23, 'Cynthia A.', 'Villar'),
                    (24, 'Juan Miguel "Migz" F.', 'Zubiri')
        """
        )

        self.__db.commit()

    def insert_items(self, items: List[Bill]) -> bool:
        cur = self.__db.cursor()
        cur.executemany(
            """
            INSERT OR IGNORE INTO bills (id, title, name, long_name, pdf, scope)
            VALUES (
                :id,
                :title,
                :name,
                :long_name,
                :pdf,
                :scope
            )
        """,
            [item.to_dict() for item in items],
        )
        values = list(chain(*[item.to_author() for item in items]))
        cur.executemany(
            """
            INSERT OR IGNORE INTO bills_authors (bills_id, authors_id)
            VALUES (:bills_id, :authors_id)
            """,
            values,
        )
        self.__db.commit()
        return True

    def close(self):
        self.__db.close()
