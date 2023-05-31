
CREATE TABLE animal
(
    id       INT NOT NULL AUTO_INCREMENT,
    name_  VARCHAR(25),
    birth DATE,
    owner_id INT NOT NULL,
    age DECIMAL,
    PRIMARY KEY (id)
);

INSERT INTO animal (name_, birth, owner_id, age)
SELECT name_, birth_date, owner_id, ROUND((ABS(year(current_date()) - year(birth_date)) + ABS(month(current_date()) - month(birth_date)) / 12), 1)
FROM dogs
UNION
SELECT name_, birth_date, owner_id, ROUND((ABS(year(current_date()) - year(birth_date)) + ABS(month(current_date()) - month(birth_date)) / 12), 1)
FROM cats
UNION
SELECT name_, birth_date, owner_id, ROUND((ABS(year(current_date()) - year(birth_date)) + ABS(month(current_date()) - month(birth_date)) / 12), 1)
FROM hamsters
UNION
SELECT name_, birth_date, owner_id, ROUND((ABS(year(current_date()) - year(birth_date)) + ABS(month(current_date()) - month(birth_date)) / 12), 1)
FROM horse
UNION
SELECT name_, birth_date, owner_id, ROUND((ABS(year(current_date()) - year(birth_date)) + ABS(month(current_date()) - month(birth_date)) / 12), 1)
FROM donkey;

CREATE TABLE young_animal
(   
    id INT NOT NULL AUTO_INCREMENT,
    name_  VARCHAR(25),
    birth DATE,
    owner_id INT NOT NULL,
    age DECIMAL,
    PRIMARY KEY (id)
);
INSERT INTO young_animal (name_, birth, owner_id, age) 
SELECT name_, birth, owner_id, age FROM animal
WHERE age BETWEEN 1.0 AND 3.0;