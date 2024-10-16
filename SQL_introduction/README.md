In this project we will be learning about SQL and how to apply it to organizing data bases.

Example Syntax:
1. Secleting data:SELECT * 
FROM employees 
WHERE department = 'Sales';
2. Inserting data:INSERT INTO employees (first_name, last_name, department, hire_date)
VALUES ('John', 'Doe', 'Marketing', '2024-01-15');
3. Updating data: UPDATE employees 
SET salary = 75000 
WHERE employee_id = 123;
4. Deleting data: DELETE FROM employees 
WHERE employee_id = 123;
5. Joining tables: SELECT e.first_name, e.last_name, d.department_name 
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
6. Grouping data: SELECT department, COUNT(*) AS employee_count 
FROM employees 
GROUP BY department;

Examples of data tables being used in SQL:
Salary Table: CREATE TABLE salaries (
    salary_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    salary DECIMAL(10, 2),
    effective_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
Employee_Project Table: CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    role VARCHAR(50),
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
