```sql
SELECT sign.user_id,
ROUND(SUM(CASE WHEN con.action = "confirmed" THEN 1 ELSE 0 END) / COUNT(CASE WHEN con.action IS NULL THEN 1 ELSE con.action END), 2) as confirmation_rate
FROM Signups as sign
LEFT JOIN Confirmations as con ON sign.user_id = con.user_id
GROUP BY sign.user_id;
```
