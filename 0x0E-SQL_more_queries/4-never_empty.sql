-- create table id_not null on mysql server
-- id_not_null
--	id INT with default value of 1
-- 	name VARCHAR(256)
-- database is passed as argument
-- if table already exist, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256));
