-- Returns: name, salary.
select name, salary from employees where (department='Engineering' or department='Marketing') and salary>70000;