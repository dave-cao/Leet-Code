```sql
# Write your MySQL query statement below
# table = Employees

SELECT unique_id, name FROM Employees as E LEFT JOIN EmployeeUNI as U ON E.id = U.id;
```
