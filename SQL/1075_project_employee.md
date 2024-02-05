```sql
SELECT p.project_id, ROUND(SUM(experience_years) / COUNT(experience_years), 2) AS average_years
FROM Project AS p
JOIN Employee as e ON p.employee_id = e.employee_id
GROUP BY project_id;
```
