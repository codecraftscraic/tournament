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

    cursor.execute('INSERT INTO Players (NAME, WINS, LOSSES) values (%s,0,0);', (name,))

    DB.commit()

    DB.close()
#5/6
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
#7
def reportMatch(winner, loser):
    #Records the outcome of a single match between two players.

    #Args:
    #  winner:  the id number of the player who won
    #  loser:  the id number of the player who lost
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Matches (WinnerID, LoserID) values (%s,%s);', (winner,loser,))

    DB.commit()

    cursor.execute('SELECT PID, WINS, LOSSES FROM Players WHERE PID = %s OR PID = %s;',(winner,loser,))
    rows = cursor.fetchall()

    #check returned PIDs against winner and loser IDs
    if rows[0][0] == winner and rows[1][0] == loser:
        wins = rows[0][1] + 1
        cursor.execute('UPDATE Players SET WINS = %s WHERE PID = %s;',(wins,winner,))
        DB.commit()

        losses = rows[1][2] + 1
        cursor.execute('UPDATE Players SET LOSSES = %s WHERE PID = %s;',(losses,loser,))
        DB.commit()
    else:
        wins = rows[1][1] + 1
        cursor.execute('UPDATE Players SET WINS = %s WHERE PID = %s;',(wins,winner,))
        DB.commit()

        losses = rows[0][2] + 1
        cursor.execute('UPDATE Players SET LOSSES = %s WHERE PID = %s;',(losses,loser,))
        DB.commit()

    DB.close()
#8
def swissPairings():
    #Returns a list of pairs of players for the next round of a match.
  
    #Assuming that there are an even number of players registered, each player
    #appears exactly once in the pairings.  Each player is paired with another
    #player with an equal or nearly-equal win record, that is, a player adjacent
    #to him or her in the standings.
  
    #Returns:
    #  A list of tuples, each of which contains (id1, name1, id2, name2)
    #    id1: the first player's unique id
    #    name1: the first player's name
    #    id2: the second player's unique id
    #    name2: the second player's name

    #enumerate() may be helpful

    DB = DB.connect()
    cursor = DB.cursor()
    playersarray = []
    matchesarray = []
    roundarray = []

    #get player info from players, and store in an array
    cursor.execute('SELECT PID,NAME,WINS FROM Players ORDER BY WINS DESC')
    playersarray = cursor.fetchall()

    #you can manipulate lists easier than tuples, fetchall returns list of tuples

    count = 0
    while 


    #get previous matches, and store in array
    cursor.execute('SELECT * FROM Matches');
    matchesarray = cursor.fetchall();

    #randomize players and return matches (for help: http://stackoverflow.com/questions/7225906/forming-random-pairs-from-a-list-sort-of)
    def player_matches (playersarray, matchesarray):
        matches = list(matchesarray);

        #where the players' wins are the same, put in separate arrays
        #go through the arrays of players one at a time, randomize, check, re-randomize if needed, else push to roundarray


        valid_match = false

        while not valid_match:
            random.shuffle(players)
    
    #function
    #check new matches to matches table
    #if matches have been played, return false
    #/function

    #if false, re-randomize
    #repeat until matches are set
    
    #once matches are set, send PID1, Name1, PID2, Name2 to array, and commit to matches and player tables
    #return array

    return roundarray;