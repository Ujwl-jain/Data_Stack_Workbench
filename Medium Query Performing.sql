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

	SELECT u.name, a.city
	FROM users u
	INNER JOIN addresses a ON u.id = a.user_id
	WHERE a.city = 'Pune';

-----------------------------------------------------------------------
--WHERE AND FILTER
-----------------------------------------------------------------------
--Q16 [MEDIUM] Fetch users whose pincode is in
--             ('411001', '400001', '110001').

	SELECT u.name,u.email, a.city, a.pincode
	FROM users u
	INNER JOIN addresses a ON u.id = a.user_id
	WHERE pincode IN ('411001', '400001', '110032');
	
--Q17 [MEDIUM] Fetch users whose name contains the word 'kumar'
--             (case-insensitive).

	SELECT * FROM users where name like '%an%'

--Q18 [MEDIUM] Fetch all users who do NOT have an address record.

	SELECT u.name, u.email
	FROM users u
	LEFT JOIN addresses a ON u.id = a.user_id
	WHERE a.user_id IS NULL;

	-- OR Subquery approach (alternative to LEFT JOIN + IS NULL)
	SELECT * FROM users
	WHERE id NOT IN (SELECT user_id FROM addresses);

--Q19 [MEDIUM] Fetch users born between 1999-01-01 and 2000-12-31.

	SELECT * FROM users WHERE date_of_birth BETWEEN '1999-01-01' and '2000-12-31';

--Q20 [MEDIUM] Fetch users whose name is exactly 5 characters long.
	
	SELECT * FROM users WHERE LEN(name) = 5;
