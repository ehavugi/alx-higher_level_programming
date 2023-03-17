-- converts hbtn_0c-0 database to UTF8 (utf8mb4, collate uft8mb4_unicode_ci)
-- converts the following
-- database  - hbtn_0c_0
-- table first_table
-- field name in first_table
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256)  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
