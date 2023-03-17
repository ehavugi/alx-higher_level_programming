-- list all Comedy shows in  hbtn_0d_tvshows database
-- use one select statement
-- each record shpuw; display tv_shows.title
-- Result must be sorted in ASC of genre name
-- db will be passed as argument
SELECT tv_shows.title AS title, tv_genres.name as name
FROM tv_genres JOIN tv_show_genres RIGHT JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
ORDER BY  title ASC, name ASC;
