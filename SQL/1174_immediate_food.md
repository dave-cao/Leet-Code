**time**: 1 hr 05 min

```sql
WITH first AS (
    SELECT customer_id, MIN(order_date) AS min
    FROM Delivery
    GROUP BY customer_id

)

SELECT
ROUND(SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date AND d.order_date = f.min THEN 1 ELSE 0 END) /
SUM(CASE WHEN d.order_date = f.min THEN 1 ELSE 0 END) * 100, 2) AS immediate_percentage
FROM Delivery as d
LEFT JOIN first as f ON f.customer_id = d.customer_id ;
```
