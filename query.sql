SELECT authors.last, bills.scope, COUNT(bills.scope) AS amount_of_bills
FROM bills
INNER JOIN bills_authors ON bills.id=bills_authors.bills_id
INNER JOIN authors ON authors.id=bills_authors.authors_id
GROUP BY authors.last, bills.scope;
-- WHERE bills_authors.authors_id=1;