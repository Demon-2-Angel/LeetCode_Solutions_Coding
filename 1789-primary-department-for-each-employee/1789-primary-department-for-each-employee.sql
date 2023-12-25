# Write your MySQL query statement below
SELECT emp1.employee_id, emp1.department_id
  FROM Employee AS emp1
 WHERE emp1.primary_flag = 'Y' OR emp1.employee_id IN   (
                                                        SELECT employee_id
                                                          FROM Employee
                                                         GROUP BY employee_id
                                                        HAVING COUNT(DISTINCT department_id) = 1
                                                        )
