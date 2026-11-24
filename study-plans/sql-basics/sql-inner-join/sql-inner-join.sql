-- Returns: name, salary, dept_name.
select employees.name, employees.salary, departments.dept_name from employees inner join departments on employees.dept_id=departments.id order by employees.name;