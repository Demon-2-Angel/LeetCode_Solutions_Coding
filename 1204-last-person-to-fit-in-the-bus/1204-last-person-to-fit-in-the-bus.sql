# Write your MySQL query statement below
SELECT q.person_name
  FROM Queue AS q
 WHERE 1000 >= (
                SELECT SUM(weight)
                  FROM Queue
                 WHERE q.turn >= turn
                )
ORDER BY turn DESC
LIMIT 1;