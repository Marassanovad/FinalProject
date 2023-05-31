
CREATE DATABASE IF NOT EXISTS humanfriends;

USE humanfriends;

## создаем таблицу хозяин

CREATE TABLE IF NOT EXISTS owners
(
    id INT NOT NULL AUTO_INCREMENT,
    name_ VARCHAR(20),
    PRIMARY KEY(id)
);

## Создаем таблицу для домашних животных

CREATE TABLE IF NOT EXISTS dogs
(
    id INT NOT NULL AUTO_INCREMENT,
    name_   VARCHAR(20) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    breed  VARCHAR(20) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS cats
(
    id INT NOT NULL AUTO_INCREMENT,
    name_   VARCHAR(20) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    breed  VARCHAR(20) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS hamsters
(
    id INT NOT NULL AUTO_INCREMENT,
    name_   VARCHAR(20) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    breed  VARCHAR(20) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

## Создаем таблицу для вьючных животных

CREATE TABLE IF NOT EXISTS horse
(
    id INT NOT NULL AUTO_INCREMENT,
    name_   VARCHAR(20) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    breed  VARCHAR(20) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS donkey
(
    id INT NOT NULL AUTO_INCREMENT,
    name_   VARCHAR(20) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS camel
(
    id INT NOT NULL AUTO_INCREMENT,
    name_   VARCHAR(20) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    birth_date DATE NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    PRIMARY KEY(id)
);

##Создаем таблицу с командами

CREATE TABLE IF NOT EXISTS commands
(
    id INT NOT NULL AUTO_INCREMENT,
    command VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
);

##Создаем таблицу для каждого животного с его командами 

CREATE TABLE IF NOT EXISTS commands_for_dog
(
    dog_id INT NOT NULL,
    command_id INT NOT NULL,
    PRIMARY KEY (dog_id, command_id),
    FOREIGN KEY (dog_id) REFERENCES dogs(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS commands_for_cat
(
    cat_id INT NOT NULL,
    command_id INT NOT NULL,
    PRIMARY KEY (cat_id, command_id),
    FOREIGN KEY (cat_id) REFERENCES cats(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS commands_for_hamster
(
    hamster_id INT NOT NULL,
    command_id INT NOT NULL,
    PRIMARY KEY (hamster_id, command_id),
    FOREIGN KEY (hamster_id) REFERENCES hamsters(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS commands_for_horse
(
    horse_id INT NOT NULL,
    command_id INT NOT NULL,
    PRIMARY KEY (horse_id, command_id),
    FOREIGN KEY (horse_id) REFERENCES horse(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS commands_for_donkey
(
    donkey_id INT NOT NULL,
    command_id INT NOT NULL,
    PRIMARY KEY (donkey_id, command_id),
    FOREIGN KEY (donkey_id) REFERENCES donkey(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS commands_for_camel
(
    camel_id INT NOT NULL,
    command_id INT NOT NULL,
    PRIMARY KEY (camel_id, command_id),
    FOREIGN KEY (camel_id) REFERENCES camel(id) ON DELETE CASCADE,
    FOREIGN KEY (command_id) REFERENCES commands(id) ON DELETE CASCADE
);