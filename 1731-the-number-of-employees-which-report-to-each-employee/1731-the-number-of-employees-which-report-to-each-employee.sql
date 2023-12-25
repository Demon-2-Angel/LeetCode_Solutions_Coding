# Write your MySQL query statement below

SELECT emp1.employee_id, emp1.name, r.reports_count, r.average_age
  FROM Employees AS emp1
 INNER JOIN (
       SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
         FROM employees
        GROUP BY reports_to
        ) AS r ON emp1.employee_id = r.reports_to
  ORDER BY emp1.employee_id;
