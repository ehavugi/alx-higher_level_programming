-- list number of records with same score in table second_table
-- result should diplay
-- 	the score
-- 	number of records for this score with lable number
SELECT score, count(*) AS number FROM second_table GROUP BY score
