-- lista ll cities in california that can be found in database
-- hbtn_0d_usa
-- states contain only 1 record name  = California(but id can be diff from ex)
-- result must be sorted by ascending order of cities.id
-- you are nnot alllowed to use join key word
-- database name will be passed as argument to msql command
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id  AND states.name = 'California'
ORDER BY cities.id ASC;
