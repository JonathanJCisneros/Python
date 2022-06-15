SELECT *
FROM books;

SELECT *
FROM favorites;

SELECT *
FROM users;

INSERT INTO users(first_name, last_name)
VALUES ('Jane', 'Amsden'),
	   ('Emily', 'Dixon'),
       ('Theodore', 'Dostoevsky'),
       ('William', 'Shapiro'),
       ('Lao', 'Xiu');
       
INSERT INTO books(title, num_of_pages)
VALUES ('C Sharp', 100),
	   ('Java', 100),
       ('Python', 100),
       ('PHP', 100),
       ('Ruby', 100);
       
UPDATE books
SET title = 'C#'
WHERE id = 1;

UPDATE users
SET first_name = 'Bill'
WHERE id = 4;

INSERT INTO favorites(user_id, books_id)
VALUES (1,1),
	   (1,2);
       
INSERT INTO favorites(user_id, books_id)
VALUES (2,1),
	   (2,2),
       (2,3);
       
INSERT INTO favorites(user_id, books_id)
VALUES (3,1),
	   (3,2),
       (3,3),
       (3,4);
       
INSERT INTO favorites(user_id, books_id)
VALUES (4,1),
	   (4,2),
       (4,3),
       (4,4),
       (4,5);

SELECT * 
FROM users
LEFT JOIN favorites ON users.id = user_id
LEFT JOIN books ON favorites.books_id = books.id
WHERE books_id = 3; 

DELETE FROM favorites
WHERE user_id = 1 AND books_id = 3;

INSERT INTO favorites (user_id, book_id) 
VALUES (5, 2);

SELECT title FROM books
JOIN favorites ON favorites.books_id = books.id
WHERE favorites.user_id = 3;

SELECT first_name, last_name FROM users
JOIN favorites ON users.id = favorites.user_id
WHERE favorites.books_id = 5;