-- Current table:

-- id NUMBER
-- city VARCHAR(21)
-- state VARCHAR(2)
-- lat_n NUMBER
-- long_w NUMBER

-----------
-- Q1:
-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
-- The STATION table is described as follows:
  
-- where LAT_N is the northern latitude and LONG_W is the western longitude.

-- For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns , because

SELECT COUNT(CITY) - COUNT(DISTINCT CITY) as unique_city FROM STATION

-----------
-- Q2: Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates. 
--   where LAT_N is the northern latitude and LONG_W is the western longitude.

SELECT DISTINCT CITY FROM STATION WHERE 
-- CITY LIKE 'A%' OR 
CITY LIKE 'a%' OR 
-- CITY LIKE 'E%' OR 
CITY LIKE 'e%' OR 
-- CITY LIKE 'I%' OR 
CITY LIKE 'i%' OR 
-- CITY LIKE 'O%' OR 
CITY LIKE 'o%' OR 
-- CITY LIKE '%U' OR 
CITY LIKE 'u%';

OR

SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '[aeiou]$';

OR

SELECT DISTINCT CITY 
FROM STATION 
WHERE RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');
  
  
