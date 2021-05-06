DROP TABLE IF EXISTS Artifact;
DROP TABLE IF EXISTS Exhibit;
DROP TABLE IF EXISTS MuseumLocation;

CREATE TABLE Artifact 
(
	ID VARCHAR(10) PRIMARY KEY, -- The primary key
    Name VARCHAR(30),
    Type VARCHAR(20),
    Description VARCHAR(2000),
    Age INT,
    ChainOCust VARCHAR(200),
    PlaceOfOrigin VARCHAR(50),
    ExhibitID VARCHAR(5),
    Value INT
);

CREATE TABLE Exhibit
(
	ID VARCHAR(5) PRIMARY KEY,
    Theme VARCHAR(100),
    MuseumLocID INT,
    LocInMuse VARCHAR(50),
    StartTime DATE,
    EndTime DATE
);

CREATE TABLE MuseumLocation
(
	ID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(100)
);

INSERT INTO Artifact VALUES ("48G3U375FT", "Ancient T-Rex Bones", "Remains", "The long lost bones of an old T-Rex.", "220000000", "Museum 1 to Museum 2", "Ancient South America", "Q674F", "10000000");
INSERT INTO Artifact VALUES ("6HK73NC83J", "European Pot", "Crafts", "An old piece of pottery from the European region.", "541", "Museum 1", "Europe", "K824T", "10000");
INSERT INTO Artifact VALUES ("C84BCU4983", "Roman Coin", "Currency", "A coin from ancient Rome.", "2000", "Museum 2 to Museum 3", "Ancient Rome", "D84NX", "8300");
INSERT INTO Artifact VALUES ("C384ND84K9", "Old Spoon", "Crafts", "A spoon from ancient Greece.", "1822", "Museum 2 to Museum 3", "Ancient Greece", "S64NX", "4000");
INSERT INTO Artifact VALUES ("E484JD94JE", "Lantern", "Crafts", "A lantern from the medival era.", "1547", "Museum 2", "Europe", "D39E4", "12000");
INSERT INTO Artifact VALUES ("EWO49398DJ", "Castle Stone", "Building", "A stone that was once part of an old castle.", "1000", "Museum 1 to Museum 3", "England", "FD7W8", "100000");
INSERT INTO Artifact VALUES ("CMEWI3R834", "Shark Tooth", "Remains", "A tooth from an ancient shark.", "200001", "Museum 2 to Museum 3", "The Vast Ocean", "34DM4", "50000");
INSERT INTO Artifact VALUES ("JREUR3RR34", "Sword", "Weapon", "A sword from medival Europe.", "800", "Museum 1", "Medival Europe", "CE84J", "25000");
INSERT INTO Artifact VALUES ("43IRI8EJ4I", "Chair", "Furniture", "A chair from Iceland", "450", "Museum 2", "Iceland", "J87CG", "7000");
INSERT INTO Artifact VALUES ("BIT49U583F", "Bow", "Weapon", "A bow from Ireland", "512", "Museum 3", "Ireland", "HJR34", "12000");
INSERT INTO Artifact VALUES ("REO9R4R439", "Mirror", "Furniture", "A mirror from Greece", "100", "Museum 2 to Museum 1", "Greece", "4HRTX", "8000");
INSERT INTO Artifact VALUES ("4380ERF490", "Diary", "Literature", "An old diary", "140", "Museum 1", "Europe", "49V9E", "80000");


INSERT INTO Exhibit VALUES ("43EIE", "Jurassic", "2389", "Floor 1, East Wing", "2020-08-10", "2020-09-10");
INSERT INTO Exhibit VALUES ("REIU8", "Arts", "4336", "Floor 2, South Wing", "2020-09-11", "2020-10-11");
INSERT INTO Exhibit VALUES ("J48J2", "Furniture", "9543", "Floor 3, West Wing", "2020-10-12", "2020-11-12");

INSERT INTO MuseumLocation VALUES ("3IUE843UE7", "Museum 1", "2874 E. Tree St");
INSERT INTO MuseumLocation VALUES ("EO9I439I3O", "Museum 2", "9454 W. Bush St");
INSERT INTO MuseumLocation VALUES ("OR3O303KOL", "Museum 3", "3209 N. Pine St");
    