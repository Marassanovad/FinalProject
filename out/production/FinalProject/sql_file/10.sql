
DELETE FROM camel;

CREATE TABLE horse_and_donkey (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY)
SELECT name_ , colour, gender, birth_date, owner_id FROM horse
UNION
SELECT name_ , colour, gender, birth_date, owner_id FROM donkey;