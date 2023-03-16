-- create hbtn_0d_usa database and table states(in hbtn_0d_usa)
-- states
--	id INT unique, autogenerated, can't be null and is a primary key
-- 	name VARCHAR(256) CAN't BE NULL
--
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
	name VARCHAR(256));
