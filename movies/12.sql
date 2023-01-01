SELECT m.title
FROM movies m
INNER JOIN stars s ON m.id = s.movie_id
INNER JOIN people p ON p.id = s.person_id
WHERE p.name = 'Johnny Depp' OR p.name = 'Helena Bonham Carter'
GROUP BY m.id
HAVING COUNT(DISTINCT p.name) = 2;