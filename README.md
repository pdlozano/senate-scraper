# Senate Scraper

This is a project that aims to scrape the Philippine Senate website for bills and laws made by Senators. It aims to show how productive each senator is because one of their main jobs is to create laws that benefit Filipinos.

To scrape it yourself, simply run the `main.py` file to update data stored in `data.sqlite`.

## How productive is each senator?

The query shown below shows us the amount of bills associated with each senator both at a local and national level.

```sql
SELECT authors.last,
       bills.scope,
       COUNT(bills.scope) AS amount_of_bills
FROM bills
         INNER JOIN bills_authors ON bills.id = bills_authors.bills_id
         INNER JOIN authors ON authors.id = bills_authors.authors_id
GROUP BY authors.last, bills.scope;
```

The result is as follows:

| Last        |  Scope   | Amount of Bills |
|:------------|:--------:|:---------------:|
| Angara      |  Local   |        2        |
| Angara      | National |       64        |
| Binay       |  Local   |        1        |
| Binay       | National |       43        |
| Cayetano    | National |       19        |
| De Lima     | National |       45        |
| Dela Rosa   | National |       13        |
| Drilon      | National |        8        |
| Gatchalian  |  Local   |        1        |
| Gatchalian  | National |       51        |
| Go          | National |       36        |
| Gordon      | National |       32        |
| Hontiveros  |  Local   |        2        |
| Hontiveros  | National |       37        |
| Lacson      | National |       14        |
| Lapid       |  Local   |       10        |
| Lapid       | National |       49        |
| Marcos      |  Local   |       58        |
| Marcos      | National |       60        |
| Pacquiao    |  Local   |        1        |
| Pacquiao    | National |       47        |
| Pangilinan  | National |       39        |
| Pimentel    | National |       29        |
| Poe         | National |       50        |
| Recto       | National |       46        |
| Revilla Jr. |  Local   |        6        |
| Revilla Jr. | National |       114       |
| Sotto III   | National |       13        |
| Tolentino   | National |       36        |
| Villanueva  |  Local   |        1        |
| Villanueva  | National |       61        |
| Villar      |  Local   |        6        |
| Villar      | National |       26        |
| Zubiri      |  Local   |        5        |
| Zubiri      | National |       35        |

This query is incomplete simply because it doesn't distinguish between primary authors and co authors. It also doesn't tell us whether the bill was passed to law which is a more important distinction of whether a senator is productive. Let us modify the query a bit to only include the bills that is in the third reading.

```sql
SELECT authors.last,
       bills.scope,
       COUNT(bills.scope) AS amount_of_bills
FROM bills
         INNER JOIN bills_authors ON bills.id = bills_authors.bills_id
         INNER JOIN authors ON authors.id = bills_authors.authors_id
WHERE bills.reading = "Third"
GROUP BY authors.last, bills.scope;
```

| Last        |  Scope   | Amount of Bills |
|:------------|:--------:|:---------------:|
| Angara      | National |        8        |
| Binay       | National |        7        |
| Cayetano    | National |        5        |
| De Lima     | National |        4        |
| Dela Rosa   | National |        4        |
| Drilon      | National |        5        |
| Gatchalian  | National |       11        |
| Go          | National |        8        |
| Gordon      | National |        9        |
| Hontiveros  | National |        5        |
| Lacson      | National |        3        |
| Lapid       | National |        6        |
| Marcos      | National |        8        |
| Pacquiao    | National |        9        |
| Pangilinan  | National |        4        |
| Pimentel    | National |        3        |
| Poe         | National |        7        |
| Recto       | National |       10        |
| Revilla Jr. | National |        9        |
| Sotto III   | National |        4        |
| Tolentino   | National |        5        |
| Villanueva  | National |       14        |
| Villar      | National |        9        |
| Zubiri      | National |       12        |

Note that there are many ways to interpret this data and this isn't everything. This data has only included bills from the 18th Congress and also doesn't include the other jobs of the senators.
