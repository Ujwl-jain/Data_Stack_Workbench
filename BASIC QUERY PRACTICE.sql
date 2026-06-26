-- SQL PRACTISE SESSION (EASY QUESTION) 

-- TABLE TO USE
-- users
SELECT * FROM users

-- addresses
SELECT * FROM addresses

-- admin_users
SELECT * FROM admin_users

-- user_log
SELECT * FROM user_log;

-----------------------------------------------------------------------
--SELECT
-----------------------------------------------------------------------

-- Q1  [BASIC]  Select all columns from the users table.
	
	SELECT * FROM users;

--Q2  [BASIC]  Select only the name and email columns from users.

	SELECT name, email FROM users;

--Q3  [BASIC]  Select the name and salary of all users, and alias
--             salary as monthly_salary.
	
	SELECT name, salary AS monthly_salary FROM users;

--Q4  [BASIC]  Fetch distinct gender values from the users table.
	
		SELECT DISTINCT gender FROM users; 

--Q5  [BASIC]  Select the top 5 users ordered by salary descending.

	SELECT TOP 5 * FROM users 
	ORDER BY salary DESC;

-----------------------------------------------------------------------
-- Where and Filters
-----------------------------------------------------------------------

--Q11 [BASIC]  Fetch all Female users from the users table.

	SELECT * FROM users WHERE gender = 'Female'

--Q12 [BASIC]  Fetch users where salary is NULL.
	
	SELECT * FROM users WHERE salary IS NULL

--Q13 [BASIC]  Fetch users where salary is NOT NULL.

SELECT * FROM users WHERE salary is NOT NULL

--Q14 [BASIC]  Fetch users with gender 'Male' AND salary greater
--             than 50000.

SELECT * FROM users WHERE gender = 'Male' AND salary > 50000;

--Q15 [BASIC]  Fetch users with city 'Mumbai' OR city 'Delhi'
--             from addresses.

SELECT * FROM addresses WHERE city = 'Mumbai' or city = 'Delhi';

-----------------------------------------------------------------------
-- Aggregate Functions
-----------------------------------------------------------------------

--Q21 [BASIC]  Count the total number of users in the users table.

	SELECT COUNT(*) AS total_users FROM users;

--Q22 [BASIC]  Find the maximum salary among all users.

	SELECT MAX(salary) as highest_earner FROM users;
	-- what if we want to check who has the max salary with name or any specific column then aggregate will not work
	
	SELECT TOP 1 name, salary FROM users ORDER BY salary DESC
	-- or using subqueries
	SELECT name, salary
	FROM users
	WHERE salary = (SELECT MAX(salary) FROM users);

--Q23 [BASIC]  Find the minimum salary among all users.

	SELECT MIN(salary) as lowest_earner FROM users;
	-- what if we want to check who has the min salary with name or any specific column then aggregate will not work
	
	SELECT TOP 1 name, salary FROM users ORDER BY salary
	--or using sub queries

	SELECT name, salary
	FROM users
	WHERE salary = (SELECT MIN(salary) FROM users);

--Q24 [BASIC]  Calculate the average salary of all users.

	SELECT AVG(salary) as avg_salary FROM users;

--Q25 [BASIC]  Find the total sum of salaries for all Male users.
	
	SELECT SUM(salary) as total_salary_expense FROM users where gender = 'Male';


-----------------------------------------------------------------------
-- DDL AND DML COMMANDS
-----------------------------------------------------------------------
--Q51 [BASIC]  Insert a new user into the users table
--             with all fields filled.
	
	INSERT INTO users(name, email, gender, date_of_birth, salary) 
	VALUES
	('Uj', 'uj@gmail.com', 'Male', '2001-07-05', 54000)


--Q52 [BASIC]  Insert a new address linked to user_id related to above question.
	
	INSERT INTO addresses(user_id, street, city, state, pincode) VALUES
	(26, 'Vishwas Nagar', 'Delhi', 'Delhi', '110032');

	-- Option 2: subquery (when you know the name but not the id)
	INSERT INTO addresses(user_id, street, city, state, pincode)
	VALUES (
		(SELECT id FROM users WHERE name = 'Uj'),
		'Some Street', 'Mumbai', 'Maharashtra', '400001');


--Q53 [BASIC]  Update the salary of user with id = 3 to 75000.

	UPDATE users SET salary = 75000 WHERE id = 3;

--Q54 [BASIC]  Delete all records from user_log where user_id is related to newly added user in above question.
	
	INSERT INTO user_log(user_id, name) VALUES
	(26, 'Uj');
	DELETE FROM user_log WHERE user_id = 26;

-----------------------------------------------------------------------
-- Subqueries
-----------------------------------------------------------------------

--Q44 [BASIC]  Find users whose salary is above the average
--             salary using a subquery.
	
	SELECT * FROM users WHERE salary > (SELECT AVG(salary) FROM users)

--Q45 [BASIC]  Find the user with the maximum salary
--             using a subquery.

	SELECT * FROM users WHERE salary = (SELECT MAX(salary) FROM users )