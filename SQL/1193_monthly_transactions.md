```sql
SELECT DATE_FORMAT(trans_date, "%Y-%m") AS month, country, COUNT(amount) AS trans_count, 
(SELECT SUM(CASE WHEN state = "approved" THEN 1 ELSE 0 END)) AS approved_count,
SUM(amount) AS trans_total_amount, 
(SELECT SUM(CASE WHEN state = "approved" THEN amount ELSE 0 END)) AS approved_total_amount
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, "%Y-%m"), country;
```
