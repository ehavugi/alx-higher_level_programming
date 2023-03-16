--  create MYSQL server user user_0d_1
-- grants all privileges on MYSQL server
-- password user_0d_1_pwd
-- should not fail if user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
