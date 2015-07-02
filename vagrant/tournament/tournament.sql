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
--WinnerID stores PID from Participants Table
	WinnerID INT NOT NULL,
--LoserID stores PID from Participants Table
	LoserID INT NOT NULL,
	CONSTRAINT pk_mid PRIMARY KEY (mid),
	CONSTRAINT fk_WinnerID FOREIGN KEY (WinnerID) REFERENCES Players (PID),
	CONSTRAINT fk_LoserID FOREIGN KEY (LoserID) REFERENCES Players (PID)
);

\q