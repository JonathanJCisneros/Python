SELECT  *
FROM countries;

SELECT *
FROM languages;

SELECT *
FROM cities;

--#1 
SELECT Name, Language, Percentage  
FROM country
LEFT JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.Language = 'Slovene'
ORDER BY countrylanguage.Percentage DESC;

--#2
SELECT country.Name AS name, COUNT(city.Name) AS cities
FROM country
LEFT JOIN city
ON country.Code = city.CountryCode
GROUP BY country.Name
ORDER BY cities DESC;

--#3
SELECT cities.name, cities.population, cities.country_id
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
WHERE countries.name = 'Mexico'
AND cities.population > 500000;

--#4
SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

--#5
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501
AND population > 100000;  

--#6
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE  government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

--#7
SELECT countries.name AS country_name, cities.name AS city_name, district, cities.population
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
WHERE district = 'Buenos Aires' AND cities.population > 500000; 

--#8
SELECT region, COUNT(name) AS countries
FROM countries
GROUP BY region
ORDER BY COUNT(name) DESC;

