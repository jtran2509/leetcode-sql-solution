# Write your MySQL query statement below
SELECT e1.name FROM Employee e1
JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY e1.name, e1.id # case when people have the same name
HAVING COUNT(*) >=5 # Use Count to include everything, even null values