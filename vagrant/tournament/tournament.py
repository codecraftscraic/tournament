#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    #Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    #Remove all the match records from the database.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('DELETE FROM Matches;')

    cursor.close()

def deletePlayers():
    #Remove all the player records from the database.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('DELETE FROM Players;')

    cursor.close()

def countPlayers():
    #Returns the number of players currently registered.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('SELECT DISTINCT * FROM Players;')

    player_count = 0

    for row in cursor:
        cursor.fetchone()
        player_count += 1

    return player_count

    cursor.close()

def registerPlayer(name):
    #Adds a player to the tournament database.
  
    #The database assigns a unique serial id number for the player.  (This
    #should be handled by your SQL database schema, not in your Python code.)
  
    #Args:
    #  name: the player's full name (need not be unique).

    DB = connect()

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Players values (name);')

    cursor.commit()

    cursor.close()

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
    playersarray = []

    cursor = DB.cursor()
    
    playersarray = cursor.execute('SELECT *, (WINS + LOSSES) AS MATCHES FROM Players ORDER BY WINS ASC;')

    return playersarray
    cursor.close()

def reportMatch(winner, loser):
    #Records the outcome of a single match between two players.

    #Args:
    #  winner:  the id number of the player who won
    #  loser:  the id number of the player who lost
    DB = connect()
    rows = []

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Matches values (' + winner + ',' + loser + ');')
    cursor.commit()

    cursor.execute('SELECT PID, WINS, LOSSES FROM Players WHERE PID = ' + winner + ' OR ' + loser + ';')
    rows = cursor.fetchall()

    #check returned PIDs against winner and loser IDs
    if rows[0][0] == winner and rows[1][0] == loser:
        wins = rows[0][1] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + winner + 'SET WINS = ' + wins + ';')
        cursor.commit()

        losses = rows[1][2] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + loser + 'SET LOSSES = ' + losses + ';')
        cursor.commit()
    else:
        wins = rows[1][1] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + winner + 'SET WINS = ' + wins + ';')
        cursor.commit()

        losses = rows[0][2] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + loser + 'SET LOSSES = ' + losses + ';')
        cursor.commit()

    cursor.close()
 