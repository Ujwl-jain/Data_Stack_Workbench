-- Performing some normal queries:

-- Fetching the data from tables
SELECT * FROM users WHERE salary > 70000
SELECT * FROM addresses WHERE state = 'Maharashtra'

-- Fetching particular columns
SELECT name, email, salary FROM users where salary > 70000
SELECT user_id,street, city, pincode FROM addresses

-- Select column as different names
SELECT name as FAMILY_MEMBERS, salary as POCKET_MONEY FROM users

-- queries using multiple operators
SELECT * FROM users where salary > 61000
SELECT * FROM users where salary < 61000
SELECT * FROM users where salary = 61000
SELECT * FROM addresses where state != 'Maharashtra'
SELECT * FROM users where salary BETWEEN 70000 AND 90000
SELECT * FROM admin_users where name LIKE 'R%'
SELECT * FROM users where date_of_birth IS NULL
SELECT * FROM users where gender IN ('Others') or gender LIKE 'Oth%'

SELECT TOP 5 * FROM users ORDER BY name DESC;
SELECT TOP 5 * FROM users;
SELECT TOP 10 * FROM users ORDER BY id DESC