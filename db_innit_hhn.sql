/*
    Initializes a database for Halloween Horror Nights by Universal Studios
*/

/* HHN initialization script */

-- drop database user if exists
DROP USER IF EXISTS 'hhn_user'@'localhost';

-- create hhn_user and grant them all the privileges to the hhn database
CREATE USER 'hhn_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'blood';

-- grant all privileges to the hhn database to the user hhn_user on localhost
GRANT ALL PRIVILEGES ON hhn.* TO 'hhn_user'@'localhost';

-- drop tables if they are present
DROP TABLE IF EXISTS attraction;
DROP TABLE IF EXISTS hhn_event;
DROP TABLE IF EXISTS attraction_location;
DROP TABLE IF EXISTS resort;
DROP TABLE IF EXISTS attraction_type;

-- create the resort table 
CREATE TABLE resort (
    resort_id     INT             NOT NULL        AUTO_INCREMENT,
    resort_name   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(resort_id)
);

-- create the attraction_location table
CREATE TABLE attraction_location (
    location_id     INT             NOT NULL        AUTO_INCREMENT,
    location_name   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(location_id)
); 

-- create the attraction_type table
CREATE TABLE attraction_type (
    type_id     INT             NOT NULL        AUTO_INCREMENT,
    type_name   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(type_id)
); 

-- create the hhn_event table
CREATE TABLE hhn_event (
    event_id     INT             NOT NULL        AUTO_INCREMENT,
    event_name   VARCHAR(75)     NOT NULL,
    event_year   VARCHAR(5)     NOT NULL,
    resort_id   INT     NOT NULL,
     
    PRIMARY KEY(event_id),

    CONSTRAINT fk_resort
    FOREIGN KEY(resort_id)
        REFERENCES resort(resort_id)
); 

-- create the attraction table and set the foreign key
CREATE TABLE attraction (
    attraction_id   INT             NOT NULL        AUTO_INCREMENT,
    attraction_name  VARCHAR(75)     NOT NULL,
    attraction_description   VARCHAR(255)     NOT NULL,
    type_id     INT      NOT NULL,
    location_id       INT     NOT NULL,
    event_id        INT     NOT NULL,

    PRIMARY KEY(attraction_id),

    CONSTRAINT fk_location
    FOREIGN KEY(location_id)
        REFERENCES attraction_location(location_id),
    
    CONSTRAINT fk_event
    FOREIGN KEY(event_id)
        REFERENCES hhn_event(event_id)
);

-- insert resort records
INSERT INTO resort (resort_name)
VALUES ('Universal Orlando'),
       ('Universal Hollywood'),
       ('Universal Singapore'),
       ('Universal Japan');

-- insert attraction_type records
INSERT INTO attraction_type (type_name)
VALUES ('House'),
       ('Scare Zone'),
       ('Show');

-- insert attraction_location records
INSERT INTO attraction_location (location_name)
VALUES ('747 Area'),
       ('Ancient Egypt'),
       ('B-108 South'),
       ('Backdraft'),
       ('Backlot Metro Sets'),
       ('Bates Motel Set'),
       ('Carnage Warehouse'),
       ('Castle Theater'),
       ('Curious George Tent 1'),
       ('Curious George Tent 2'),
       ('Earthquake/Disaster Queue'),
       ('Emporium'),
       ('Fast and Furious'),
       ('FDTD Area'),
       ('Fievel''s Playland'),
       ('French Street'),
       ('House of Horrors'),
       ('Jaws Queue'),
       ('Jurassic Park Discovery Center'),
       ('Jurassic Park Queue'),
       ('Jurassic Park Tent'),
       ('Lower Lot'),
       ('Men in Black Tent'),
       ('Minions Mayhem'),
       ('Moulin Rouge'),
       ('Mummy Queue'),
       ('Nazarman''s'),
       ('New York'),
       ('Palace Theater'),
       ('Parade Building'),
       ('Parisian Courtyard'),
       ('Popeye and Bluto''s Blige-Rat Barges Queue'),
       ('Poseidon''s Fury'),
       ('Rockefeller City Tent'),
       ('San Francisco'),
       ('Shrek 4D'),
       ('Shrek 4D Queue'),
       ('Soundstage 15'),
       ('Soundstage 18'),
       ('Soundstage 19'),
       ('Soundstage 20'),
       ('Soundstage 21'),
       ('Soundstage 22'),
       ('Soundstage 23'),
       ('Soundstage 24'),
       ('Soundstage 25'),
       ('Soundstage 28'),
       ('Soundstage 29'),
       ('Soundstage 34'),
       ('Soundstage 36'),
       ('Soundstage 44'),
       ('Space Fantasy'),
       ('Sprung Tent 1'),
       ('Sprung Tent 2'),
       ('Stage 18'),
       ('Stage 22'),
       ('Sting Alley'),
       ('Terminator Queue'),
       ('Terror Tram'),
       ('The Boneyard'),
       ('The Obelisk'),
       ('Thunder Falls Terrace'),
       ('Tram Warehouse'),
       ('Triceratops Encounter'),
       ('Upper Lot'),
       ('Waterworld'),
       ('Wild Wild West Stage'),
       ('Amity'),
       ('Avenue of the Stars'),
       ('Backlot'),
       ('Backlot Tunnel'),
       ('Baker Street'),
       ('Central Park'),
       ('Front Gate'),
       ('Front Lot'),
       ('Gramercy Park'),
       ('Hollywood'),
       ('Jurassic Park'),
       ('Marvel Super Hero Island'),
       ('Park-Wide'),
       ('Port of Entry'),
       ('Sci-Fi City'),
       ('Shrek Alley'),
       ('South Street'),
       ('Seuss Landing'),
       ('The Lost Continent'),
       ('The Lost World'),
       ('Toon Lagoon'),
       ('Western Street'),
       ('Woody Woodpecker Kidzone'),
       ('World Expo'),
       ('An American Tale Live'),
       ('Animal Actors'),
       ('Beetlejuice''s Graveyard Revue Stage'),
       ('Blues Brothers'),
       ('Cinema 4d'),
       ('Delancey Street'),
       ('Enchanted Oak Tavern'),
       ('Fear Factor Live Stage'),
       ('Hollywood Lagoon Stage'),
       ('Main Entrance'),
       ('Mel''s Die-In'),
       ('Metropolis Tribune'),
       ('New York Public Library'),
       ('Pantages Theater'),
       ('Special Effects Stage'),
       ('Terminator 3D'),
       ('Toon Ampitheater'),
       ('USF Lagoon'),
       ('Victoria Station'),
       ('War Lord Tower'),
       ('Wild West Stunt Show'),
       ('Unknown');




