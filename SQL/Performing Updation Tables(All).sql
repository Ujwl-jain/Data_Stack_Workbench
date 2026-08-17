-- Performing Updation on tables

SELECT * FROM users
SELECT * FROM admin_users
SELECT * FROM addresses
SELECT * FROM user_log

-------------------------------
--UPDATING TABLES USING SET AND ROLLBACK METHOD FOR THE LOVE OF THE GAME

BEGIN TRANSACTION;

UPDATE users SET salary = NULL WHERE id = 6

ROLLBACK;

SELECT * FROM users WHERE salary IS NULL

-- COMMIT;




