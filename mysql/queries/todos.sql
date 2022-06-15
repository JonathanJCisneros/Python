SELECT *
FROM todos;

SELECT *
FROM users;

SELECT users.first_name, users.last_name, todos.todo, todos.status
FROM users JOIN todos ON users.id = todos.user_id
-- 	JOIN carts ON carts.id = todos.id
WHERE todos.status = 'Complete';

SELECT users.first_name, users.last_name, todos.todo, todos.status
FROM users, todos
WHERE users.id = todos.user_id AND todos.status = 'Complete';

SELECT *
FROM users LEFT JOIN todos ON users.id = todos.user_id;