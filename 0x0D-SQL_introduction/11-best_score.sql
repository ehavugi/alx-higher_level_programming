-- lists all records with score >=10 from the second_table table,
-- table of hbtn_0c_0
-- should display both score and name (in this order)
-- order by score top first
-- db name will be passed to mysql
SELECT score, name FROM second_table where score >= 10 ORDER BY score DESC;
