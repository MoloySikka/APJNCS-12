use db;

desc emp;
select * from emp;

select count(*) 'Number of records' from emp;

select count(city) 'Non-null cities' from emp;
select count(distinct city) 'Distinct cities' from emp;

select dept_id 'Department', count(*) 'Number of records' from emp group by dept_id;

select dept_id 'Departments having total salary > 500000' from emp group by dept_id having sum(salary) > 500000;

select dept_id, avg(salary) 'Average salary' from emp group by dept_id;

select min(salary) 'Min salary', max(salary) 'Max salary' from emp;
