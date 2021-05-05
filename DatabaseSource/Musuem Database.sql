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

INSERT INTO Artifact VALUES ("48G3U375FT", "Ancient T-Rex Bones", "Remains", "The long lost bones of an old T-Rex", "220000000", "Museum 1 to Museum 2", "Ancient South America", "Q674F", "10000000");
    