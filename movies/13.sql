SELECT p.name
FROM movies m
INNER JOIN stars s ON m.id = s.movie_id
INNER JOIN people p ON p.id = s.person_id
INNER JOIN stars s2 ON m.id = s2.movie_id
INNER JOIN people p2 ON p2.id = s2.person_id
WHERE p2.name = 'Kevin Bacon' AND p2.birth = 1958 AND p.name != 'Kevin Bacon'
GROUP BY p.id;