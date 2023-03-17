-- List all genres not linked to show Dexter
-- record should display tv_genres.name
-- Result must be sorted in ASC of genre name
-- db will be passed as argument
-- can use a maximum of two SELECT statements
-- it usss 3 tables tv_genres, tv_show_genres, tv_shows inner joins were used
SELECT DISTINCT tv_genres.name AS name
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
WHERE name NOT IN (
SELECT tv_genres.name 
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY  name ASC;
