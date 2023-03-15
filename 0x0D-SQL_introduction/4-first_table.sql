-- create a table called first_table in current db in MYSQL
-- first_table description
--    id INT
--    name VARHCAR(256)
-- without using SELECT or SHOW commands
-- show not cause error if table exists
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
