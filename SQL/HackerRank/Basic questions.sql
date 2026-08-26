-- Current table: STATION

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
  WHERE CITY REGEXP '^[aeiou]';
  
  OR
  
  SELECT DISTINCT CITY 
  FROM STATION 
  WHERE LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');

-----------
-- Q3: Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

  SELECT DISTINCT CITY 
  FROM STATION 
  WHERE CITY REGEXP '[aeiou]$';

  OR
    
  SELECT DISTINCT CITY 
  FROM STATION 
  WHERE RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');

-----------
-- Q4. Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

SELECT CITY, LENGTH(CITY)
FROM STATION ORDER BY 
LENGTH(CITY) ASC, CITY ASC
LIMIT 1;

SELECT CITY, LENGTH(CITY) 
FROM STATION ORDER BY 
LENGTH(CITY) DESC, CITY ASC
LIMIT 1;

-----------
-- Q5.   Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

  SELECT DISTINCT CITY 
  FROM STATION 
  WHERE LOWER(LEFT(CITY, 1)) IN ('a', 'e', 'i', 'o', 'u') 
  AND LOWER(RIGHT(CITY, 1)) IN ('a', 'e', 'i', 'o', 'u');

-----------------------
-- Q6. Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(LEFT(CITY, 1)) NOT IN ('a','e','i', 'o', 'u');

----------
-- Q7. Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(RIGHT(CITY, 1)) NOT IN ('a','e','i', 'o', 'u');

---------
-- Q8. Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(LEFT(CITY,1)) NOT IN ('a', 'e', 'i', 'o', 'u') OR
LOWER(RIGHT(CITY,1)) NOT IN ('a', 'e', 'i', 'o', 'u');

---------
-- Q9. Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(LEFT(CITY,1)) NOT IN ('a', 'e', 'i', 'o', 'u') AND
LOWER(RIGHT(CITY,1)) NOT IN ('a', 'e', 'i', 'o', 'u');

---------
-- Q10. Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.

SELECT ROUND(SUM(LAT_N),4) FROM STATION 
WHERE 
LAT_N > 38.7880 AND LAT_N < 137.2345

---------
  -- Q11. Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.
  
SELECT ROUND(LAT_N,4) FROM STATION
WHERE
LAT_N < 137.2345 
ORDER BY LAT_N DESC 
LIMIT 1 

---------
-- Q12. Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.

SELECT ROUND(LONG_W,4) FROM STATION
WHERE LAT_N < 137.2345 
ORDER BY LAT_N DESC
LIMIT 1

---------
-- Q13. Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to 4 decimal places.

SELECT ROUND(LAT_N, 4) FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1

---------
-- Q14. Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.

SELECT ROUND(LONG_W,4) FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1;

---------
-- Q15. Query the following two values from the STATION table:

-- The sum of all values in LAT_N rounded to a scale of 2 decimal places.
-- The sum of all values in LONG_W rounded to a scale of 2 decimal places.

SELECT ROUND(SUM(LAT_N),2) AS lat, 
ROUND(SUM(LONG_W),2) AS lon
FROM STATION

--------------------------------------------------------------------------------------
-- Table: CITY
--   ID = NUMBER
--   NAME = VARCHAR2(17)
--   COUNTRYCODE = VARCHAR2(3)
--   DISTRICT = VARCHAR2(20)
--   POPULATION = NUMBER
-- Q16.  Query a count of the number of cities in CITY having a Population larger than .
SELECT COUNT(DISTINCT(NAME)) FROM CITY
WHERE POPULATION > 100000

---------
-- Q17. Query the total population of all cities in CITY where District is California.

SELECT SUM(POPULATION) FROM CITY
WHERE DISTRICT = 'California';

---------
-- Q18. Query the average population of all cities in CITY where District is California.

SELECT AVG(POPULATION) FROM CITY
WHERE DISTRICT = 'California';

---------
-- Q19. Query the average population for all cities in CITY, rounded down to the nearest integer.

  SELECT ROUND(AVG(POPULATION)) FROM CITY;

---------
-- Q20. Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

SELECT SUM(POPULATION) FROM CITY
WHERE COUNTRYCODE = 'JPN';
