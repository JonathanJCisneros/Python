SELECT *
FROM users;

SELECT *
FROM friendships;

INSERT INTO users (first_name, last_name)
VALUES ('Kevin','Bacon'),
	   ('Henry','Ford'),
       ('Dwyane','Johnson'),
       ('Chris','Pratt'),
       ('Emily','Nunez'),
       ('Anthony','Williams');

INSERT INTO friendships (user_id,friend_id)
VALUES (1,2),
	   (1,4),
       (1,6),
       (2,1),
       (2,3),
       (2,5),
       (3,2),
       (3,5),
       (4,3),
       (5,1),
       (5,6),
       (6,2),
       (6,3);

SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name 
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;


SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id = 1;

SELECT COUNT(*) as num_of_friendships from friendships;

