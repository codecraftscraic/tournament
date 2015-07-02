udacity_relational_databases_tournament_project

Nanodegree Project

Files
-----

tournament.py: my implementation of the assigned Swiss-System style of tourmament.
tournament.sql: my implementation of the database schema for the tournament database.
tournament_test.py: tests for project provided by Udacity.

Execution
---------

Initialize the database/ensure it exists

```
vagrant@vagrant-ubuntu-trusty-32:~$ psql
psql (9.3.9)
Type "help" for help.

vagrant=> \i tournament.sql
vagrant=> \q
```

Change directories into the tournament folder

```
vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant
vagrant@vagrant-ubuntu-trusty-32:/vagrant$cd tournament
```

Run tournament_test.py

```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```
