
CREATE TABLE all_animal
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
)
SELECT name_, birth_date, colour, gender, owner_id FROM dogs
UNION
SELECT name_, birth_date, colour, gender, owner_id FROM cats
UNION
SELECT name_, birth_date, colour, gender, owner_id FROM hamsters
UNION
SELECT name_, birth_date, colour, gender, owner_id FROM horse
UNION
SELECT name_, birth_date, colour, gender, owner_id FROM donkey;
