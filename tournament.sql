-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

DROP TABLE IF EXISTS Players CASCADE;

CREATE TABLE Players (
	PID SERIAL,
	NAME TEXT NOT NULL,
	CONSTRAINT pk_pid PRIMARY KEY (pid)
);

DROP TABLE IF EXISTS Matches CASCADE;

CREATE TABLE Matches (
	MID SERIAL,
--WinnerID stores PID from Participants Table
	WinnerID INT NOT NULL,
--LoserID stores PID from Participants Table
	LoserID INT NOT NULL,
	CONSTRAINT pk_mid PRIMARY KEY (mid),
	CONSTRAINT fk_WinnerID FOREIGN KEY (WinnerID) REFERENCES Players (PID),
	CONSTRAINT fk_LoserID FOREIGN KEY (LoserID) REFERENCES Players (PID)
);

DROP VIEW IF EXISTS Totals CASCADE;

CREATE VIEW Totals AS

	SELECT PID,NAME, COUNT(WINS.*) AS TOTALWINS, COUNT(LOSSES.*) AS TOTALLOSSES 
		FROM Players LEFT JOIN Matches AS WINS ON Players.PID = WINS.WinnerID 
		LEFT JOIN Matches AS LOSSES ON Players.PID = LOSSES.LoserID GROUP BY PID;

\q











