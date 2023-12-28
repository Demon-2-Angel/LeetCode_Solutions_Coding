WITH cnt AS (
    SELECT user_id, COUNT(movie_id) AS count
      FROM MovieRating
     GROUP BY user_id
),

avg1 AS (
    SELECT movie_id, AVG(rating) AS AVG
      FROM MovieRating
     WHERE EXTRACT(YEAR_MONTH FROM created_at) = 202002
     GROUP BY movie_id
)

(SELECT name AS results
  FROM Users
  JOIN cnt ON Users.user_id = cnt.user_id
 WHERE cnt.count = (SELECT MAX(count) FROM cnt)
 ORDER BY name
 LIMIT 1)

 UNION ALL
(
SELECT title AS results
  FROM Movies
  JOIN avg1 ON Movies.movie_id = avg1.movie_id
  WHERE avg1.AVG = (SELECT MAX(AVG) FROM avg1)
  ORDER BY title
  LIMIT 1);