-- list all records of table second_table 
-- don't list rows with a name value
-- results should display score, and name in that order
-- list by descending score 
-- database name will be passed as an argument to the mysql command
SELECT score, name FROM second_table where name IS NOT NULL ORDER BY score DESC;
