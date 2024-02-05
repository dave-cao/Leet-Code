```sql
WITH m_count AS
(SELECT id, managerId, COUNT(managerId) as manager_count
FROM Employee
GROUP BY managerId)

SELECT e.name 
FROM m_count
JOIN Employee AS e ON e.id = m_count.managerId
WHERE m_count.manager_count >= 5;
```
