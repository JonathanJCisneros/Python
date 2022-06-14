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
VALUES('Jonathan', 'Cisneros', 25, 1),
	  
