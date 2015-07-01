#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    #Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")

#1
def deleteMatches():
    #Remove all the match records from the database.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('TRUNCATE TABLE Matches;')

    DB.commit()

    DB.close()
#2
def deletePlayers():
    #Remove all the player records from the database.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('TRUNCATE TABLE Players CASCADE;')

    DB.commit()

    DB.close()
#3
def countPlayers():
    #Returns the number of players currently registered.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('SELECT COUNT(PID) FROM Players;')

    player_count = cursor.fetchall()

    DB.close()

    return player_count[0][0]
#4
def registerPlayer(name):
    #Adds a player to the tournament database.
  
    #The database assigns a unique serial id number for the player.  (This
    #should be handled by your SQL database schema, not in your Python code.)
  
    #Args:
    #  name: the player's full name (need not be unique).

    DB = connect()

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Players (NAME, WINS, LOSSES) values (\'' + name + '\',0,0);')

    DB.commit()

    DB.close()
#5
def playerStandings():
    #Returns a list of the players and their win records, sorted by wins.

    #The first entry in the list should be the player in first place, or a player
    #tied for first place if there is currently a tie.

    #Returns:
    #  A list of tuples, each of which contains (id, name, wins, matches):
    #    id: the player's unique id (assigned by the database)
    #    name: the player's full name (as registered)
    #    wins: the number of matches the player has won
    #    matches: the number of matches the player has played
    DB = connect()

    cursor = DB.cursor()
    
    cursor.execute('SELECT PID, NAME, WINS, (WINS + LOSSES) as MATCHES FROM Players ORDER BY WINS DESC;')

    playersarray = cursor.fetchall()

    DB.close()
    
    return playersarray
#6
def reportMatch(winner, loser):
    #Records the outcome of a single match between two players.

    #Args:
    #  winner:  the id number of the player who won
    #  loser:  the id number of the player who lost
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Matches (WinnerID, LoserID) values (%d,%d);', (winner,loser))
    DB.commit()

    DB.close()
 


















