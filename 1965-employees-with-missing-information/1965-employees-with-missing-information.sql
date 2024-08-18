# Write your MySQL query statement below

select e.employee_id
from Employees e natural left join Salaries s
where S.salary is null
union
select s.employee_id
from Salaries s natural left join Employees e
where e.name is null
order by employee_id;