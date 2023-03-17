-- list all shows in hbtn_0d_tv_shows that have at least 1 genre linked
-- each record display tv_show.title -- tv_show_genres.genre_id
-- results should be sorted in 
-- ascending order by tv_shows.title and tv_show_genre_id
-- use one select statement
-- db will be passed as argument
SELECT tv_shows.title AS title , tv_show_genres.genre_id AS genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
