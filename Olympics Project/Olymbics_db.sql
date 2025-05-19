CREATE TABLE noc_regions (
    NOC VARCHAR(3) PRIMARY KEY,
    Region VARCHAR(50),
    Notes VARCHAR(50)
);

CREATE TABLE games (
    GameID INT AUTO_INCREMENT PRIMARY KEY,
    Year INT,
    Season VARCHAR(50)
);

CREATE TABLE athlete_events (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Sex VARCHAR(50),
    Age INT,
    Height INT,
    Weight INT,
    Team VARCHAR(50),
    NOC VARCHAR(3),
    GameID INT,
    City VARCHAR(50),
    Sport VARCHAR(50),
    Event VARCHAR(50),
    Medal VARCHAR(50),

    FOREIGN KEY (NOC) REFERENCES noc_regions(NOC),
    FOREIGN KEY (GameID) REFERENCES games(GameID)
);