DROP TABLE IF EXISTS "Coach";
CREATE TABLE Coach
(cID INTEGER,
 name CHAR(10),
 tName CHAR(10),
 cName CHAR(10),
PRIMARY KEY (cID));
INSERT INTO "Coach" VALUES(1,'thara','UK','peru');
INSERT INTO "Coach" VALUES(2,'dennis','india','mexico');
INSERT INTO "Coach" VALUES(3,'jessy','brazil','india');
INSERT INTO "Coach" VALUES(4,'savio','mexico','UK');
INSERT INTO "Coach" VALUES(5,'mathew','peru','brazil');
DROP TABLE IF EXISTS "Country";
CREATE TABLE Country
( cname CHAR(100),
 language CHAR(100),
capital  CHAR(100),
 poulation INTEGER,
PRIMARY KEY (cname,language)
  );
INSERT INTO "Country" VALUES('india','hindi','delhi',350000);
INSERT INTO "Country" VALUES('UK','english','london',25000);
INSERT INTO "Country" VALUES('brazil','brazilian','brazilcity',350000);
INSERT INTO "Country" VALUES('peru','perian','peru',34000);
INSERT INTO "Country" VALUES('mexico','mexican','mexicocity',100000);
DROP TABLE IF EXISTS "Game";
CREATE TABLE Game
( team1 CHAR(10),
team2 CHAR(10),
stadium CHAR(10),
result CHAR(10),
PRIMARY KEY (team1,team2)
);
INSERT INTO "Game" VALUES('india','UK','londonstadium','won');
INSERT INTO "Game" VALUES('UK','brazil','brazilstadium','won');
INSERT INTO "Game" VALUES('brazil','india','perustadium','draw');
INSERT INTO "Game" VALUES('brazil','mexico','mexicostadium','won');
INSERT INTO "Game" VALUES('india','mexico','mexicostadium','won');
INSERT INTO "Game" VALUES('peru','india','brazilstadium','won');
INSERT INTO "Game" VALUES('brazil','peru','londonstadium','draw');
DROP TABLE IF EXISTS "Player";
CREATE TABLE Player
(pID INTEGER,
 name CHAR(10),
 tName CHAR(10),
 position CHAR(10),
 goals INTEGER,
PRIMARY KEY (pID));
INSERT INTO "Player" VALUES(101,'vivek','UK','Defender',10);
INSERT INTO "Player" VALUES(102,'novina','india','attacker',12);
INSERT INTO "Player" VALUES(103,'sukanya','brazil','attacker',15);
INSERT INTO "Player" VALUES(104,'wei','peru','keeper',20);
INSERT INTO "Player" VALUES(105,'kavi','mexico','attacker',25);
INSERT INTO "Player" VALUES(106,'christine','india','attacker',18);
INSERT INTO "Player" VALUES(107,'megha','india','defender',28);
DROP TABLE IF EXISTS "Stadium";
CREATE TABLE Stadium
 (name CHAR (10),
 capacity CHAR (10),
 location CHAR (10),
PRIMARY KEY (name));
INSERT INTO "Stadium" VALUES('londonstadium','2500','london');
INSERT INTO "Stadium" VALUES('brazilstadium','1500','brazilcity');
INSERT INTO "Stadium" VALUES('perustadium','2100','peru');
INSERT INTO "Stadium" VALUES('mexicostadium','4000','mexicocity');
DROP TABLE IF EXISTS "Team";
CREATE TABLE Team
 (tName CHAR(10),
 color CHAR(10),
 goals INTEGER,
 groupname CHAR(10),
PRIMARY KEY (tName)
);
INSERT INTO "Team" VALUES('india','blue',78,'A');
INSERT INTO "Team" VALUES('UK','red',69,'B');
INSERT INTO "Team" VALUES('peru','white',50,'A');
INSERT INTO "Team" VALUES('brazil','yellow',67,'B');
INSERT INTO "Team" VALUES('mexico','black',20,'B');
CREATE VIEW tableB AS
 SELECT team1 FROM Game
  UNION
 SELECT team2 FROM Game;
CREATE VIEW tablea AS
 SELECT team1 FROM Game;
