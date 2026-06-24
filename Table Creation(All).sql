--CREATE TABLE users (
--    id INT IDENTITY(1,1) PRIMARY KEY,
--    name VARCHAR(100) NOT NULL,
--    email VARCHAR(100) UNIQUE NOT NULL,
--    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
--    date_of_birth DATE,
--    salary DECIMAL(10,2),
--    created_at DATETIME2 DEFAULT SYSDATETIME()
--);

-- admin table
--CREATE TABLE admin_users (
--    id INT IDENTITY(1,1) PRIMARY KEY,   -- Added IDENTITY (recommended)
--    name VARCHAR(100),
--    email VARCHAR(100),
--    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')),
--    date_of_birth DATE,
--    salary INT
--);

-- Addressess Tables

--CREATE TABLE addresses (
--    id INT IDENTITY(1,1) PRIMARY KEY,
--    user_id INT,
--    street VARCHAR(255),
--    city VARCHAR(100),
--    state VARCHAR(100),
--    pincode VARCHAR(10),
--    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) 
--        ON DELETE CASCADE
--);



SELECT * FROM users;
SELECT * FROM admin_users;
SELECT * FROM addresses


