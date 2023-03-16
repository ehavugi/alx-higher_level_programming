-- list cities by states
-- each record dispolay cities.id -- cities.name -- states.name
-- results should be sorted by cities.id
-- use on select statement
-- database name will be passed as argument
SELECT cities.id, cities.name, states.name
FROM states,cities
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
