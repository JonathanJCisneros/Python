-- 1 

SELECT customer.first_name AS first_name, customer.last_name AS last_name, customer.email AS email, address.address AS address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON address.city_id = city.city_id
WHERE city.city_id = 312;

-- 2

SELECT title, description, release_year, rating, special_features, category.name AS genre
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

-- 3

SELECT  actor.actor_id AS actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name, film.title AS title, film.description AS description, film.release_year AS release_year
FROM actor
LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
LEFT JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5; 

-- 4

SELECT customer.first_name AS first_name, customer.last_name AS last_name, customer.email AS email, CONCAT(' ', address.address, address.address2) AS address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
WHERE customer.store_id = 1 AND address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459;

-- 5

SELECT film.title AS title, film.description AS description, film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 15 AND film.rating = "G" AND film.special_features LIKE "%Behind the Scenes%";

-- 6

SELECT film.film_id AS film_id, film.title AS title, actor.actor_id AS actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name
FROM film
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369; 

-- 7

SELECT film.title AS title, film.description AS description, film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 AND category.name = "Drama"; 

-- 8

SELECT film.title AS title, film.description AS description, film.release_year AS release_year, film.rating AS rating, film.special_features AS special_features, category.name AS genre, CONCAT(' ', actor.first_name, actor.last_name) AS actor_name
FROM film
LEFT JOIN film_category
ON film.film_id = film_category.film_id
LEFT JOIN category
ON film_category.category_id = category.category_id
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE category.name = "Action" AND concat_ws(' ', actor.first_name, actor.last_name) = "SANDRA KILMER";
