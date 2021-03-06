SELECT * 
FROM dojos;

SELECT *
FROM ninjas;

INSERT INTO dojos(name)
VALUES('Karate'),
	  ('TaeKwonDo'),
      ('Tai Chi');
      
DELETE FROM dojos
WHERE id > 0; 

INSERT INTO dojos(name)
VALUES('Coding'),
	  ('Anime'),
      ('Real');
      
INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES('Jonathan', 'Cisneros', 25, 4),
	  ('Kevin', 'Orozco', 29, 4),
      ('Ashley', 'Reyes', 35, 4);
      
INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES('Sean', 'Kroft', 22, 5),
	  ('Stef', 'Something', 29, 5),
      ('Carol', 'Baskin', 35, 5);
      
INSERT INTO ninjas(first_name, last_name, age, dojo_id)
VALUES('Andy', 'Wilson', 25, 6),
	  ('Arron', 'Nguyen', 21, 6),
      ('Bill', 'Shell', 65, 6);
      
SELECT *
FROM ninjas
WHERE dojo_id = 4;

SELECT dojos.name
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 12;