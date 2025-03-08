SET FOREIGN_KEY_CHECKS = 0;

-- Load Player data
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/players.csv'
INTO TABLE Player
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

-- Load Team data
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/teams.csv'
INTO TABLE Team
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

-- Load Tournament data
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/tournaments.csv'
INTO TABLE Tournament
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

-- Load GameMatch data
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/matches.csv'
INTO TABLE GameMatch
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

-- Load Statistics data
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/statistics.csv'
INTO TABLE Statistics
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

-- Load Relationship Tables
LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/has_player.csv'
INTO TABLE has_player
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/invited_to.csv'
INTO TABLE invited_to
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/competes_in.csv'
INTO TABLE competes_in
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/participates_in.csv'
INTO TABLE participates_in
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/contains.csv'
INTO TABLE contains
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/achieves.csv'
INTO TABLE achieves
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.1/Uploads/generates.csv'
INTO TABLE generates
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n';

SET FOREIGN_KEY_CHECKS = 1;
