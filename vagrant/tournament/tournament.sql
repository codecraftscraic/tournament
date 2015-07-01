-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE DATABASE tournament;

\c tournament;

CREATE TABLE Players (
	PID SERIAL NOT NULL,
	NAME TEXT NOT NULL,
	WINS INT,
	LOSSES INT,
	CONSTRAINT pk_pid PRIMARY KEY (pid)
);

CREATE TABLE Matches (
	MID SERIAL NOT NULL,
--Commenting out for now. Worry about extra credit later
	--TID INT FOREIGN KEY NOT NULL,
--WinnerID stores PID from Participants Table
	WinnerID INT NOT NULL,
--LoserID stores PID from Participants Table
	LoserID INT NOT NULL,
	CONSTRAINT pk_mid PRIMARY KEY (mid),
	CONSTRAINT fk_WinnerID FOREIGN KEY (WinnerID) REFERENCES Players (PID),
	CONSTRAINT fk_LoserID FOREIGN KEY (LoserID) REFERENCES Players (PID)
);

--Commenting out for now. Worry about extra credit later
--CREATE TABLE Tournaments {
--	TID INT PRIMARY KEY NOT NULL autofill unsigned,
--	MID INT FOREIGN KEY NOT NULL,
--TournWinner stores PID of tournament winner from Participants Table
--	TournWinner INT FOREIGN KEY
--}

\q