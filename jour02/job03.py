# mysql> insert into etage (nom, numero, superficie)
#     -> values
#     -> "RDC", 0, 500),
#     -> "RDC", 0, 500),\c
# mysql> insert into etage (nom, numero, superficie)
#     -> values
#     -> ("RDC", 0, 500),
#     -> ("R+1", 1, 500);
# Query OK, 2 rows affected (0.01 sec)
# Records: 2  Duplicates: 0  Warnings: 0

# mysql> select * from etage;
# +----+------+--------+------------+
# | id | nom  | numero | superficie |
# +----+------+--------+------------+
# |  1 | RDC  |      0 |        500 |
# |  2 | R+1  |      1 |        500 |
# +----+------+--------+------------+
# 2 rows in set (0.00 sec)

# mysql> insert into salles (nom, id_etage, capacite)
#     -> ("Lounge", 1, 100),
#     -> ("Studio son", 1, 5),
#     -> ("Studio son", 1, 5),\c
# mysql> insert into salles (nom, id_etage, capacite)
#     -> values
#     -> ("Lounge", 1, 100),
#     -> ("Studio son", 1, 5),
#     -> ("Broadcasting", 2, 50),
#     -> ("Bocal Peda", 2, 4),
#     -> ("Coworking", 2, 80),
#     -> ("Studio Video", 2, 5);
# Query OK, 6 rows affected (0.01 sec)
# Records: 6  Duplicates: 0  Warnings: 0

# mysql> select * from salles;
# +----+--------------+----------+----------+
# | id | nom          | id_etage | capacite |
# +----+--------------+----------+----------+
# |  1 | Lounge       |        1 |      100 |
# |  2 | Studio son   |        1 |        5 |
# |  3 | Broadcasting |        2 |       50 |
# |  4 | Bocal Peda   |        2 |        4 |
# |  5 | Coworking    |        2 |       80 |
# |  6 | Studio Video |        2 |        5 |
# +----+--------------+----------+----------+
# 6 rows in set (0.00 sec)