-- list all genres of show Dexter from hbtn_0d_tvshows
-- tv_shows contains only one record where title = Dexter
-- use one select statement
-- Result must be sorted in ASC of genre name
-- db will be passed as argument
-- it usss 3 tables tv_genres, tv_show_genres, tv_shows inner joins were used
SELECT tv_genres.name AS name
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY  name ASC;
