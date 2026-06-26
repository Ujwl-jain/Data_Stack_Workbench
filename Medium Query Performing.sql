-- SQL PRACTISE SESSION (Medium QUESTION) 

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
--Q6  [MEDIUM] Select all users created after January 1, 2024.

	SELECT id, name FROM users WHERE created_at >= '2024-06-20'
	
--Q7  [MEDIUM] Select users whose salary is between 30000 and 70000.

	SELECT * FROM users WHERE salary BETWEEN 40000 AND 50000

--Q8  [MEDIUM] Select users whose name starts with the letter 'A'.

	SELECT id, name FROM users WHERE name LIKE 'A%'

--Q9  [MEDIUM] Select all users where email ends with '@gmail.com'.

	SELECT * FROM users WHERE email LIKE '%@gmail.com'

--Q10 [MEDIUM] Select name and city from users joined with addresses,
--             for users in the city 'Pune'.
