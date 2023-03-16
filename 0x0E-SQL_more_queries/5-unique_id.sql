-- create table unique_id on mysql server
-- unique_id
--	id INT with default vaue of 1 and must be unique
-- 	name VARCHAR(256)
-- 
CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
