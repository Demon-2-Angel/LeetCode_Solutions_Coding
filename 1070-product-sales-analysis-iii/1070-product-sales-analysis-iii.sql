# Write your MySQL query statement below
select s.product_id, s.year first_year, s.quantity, s.price
  from Sales s
 where (s.product_id, s.year) in (
                                    Select product_id, min(year) from Sales 
                                     group by product_id)