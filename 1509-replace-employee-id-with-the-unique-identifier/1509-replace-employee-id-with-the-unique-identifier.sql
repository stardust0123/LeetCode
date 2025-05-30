# Write your MySQL query statement below
SELECT name, unique_id FROM Employees 
LEFT JOIN EmployeeUNi 
ON employees.id = employeeuni.id