# Write your MySQL query statement below
select unique_id, name FROM EmployeeUNI 
RIGHT JOIN Employees ON EmployeeUNI.id = Employees.id
