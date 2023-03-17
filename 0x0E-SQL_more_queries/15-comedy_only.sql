-- list all Comedy shows in  hbtn_0d_tvshows database
-- use one select statement
-- each record shpuw; display tv_shows.title
-- Result must be sorted in ASC of genre name
-- db will be passed as argument
SELECT tv_shows.title AS title
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY  title ASC;
