# mysql> use laplateforme;
# Database changed
# mysql> create table etage
#     -> (id int primary key auto_increment,
#     -> nom varchar(255),
#     -> numero int,
#     -> superficie int);
# Query OK, 0 rows affected (0.01 sec)

# mysql> create table salles
#     -> (id int primary key auto_increment,
#     -> nom varchar(255),
#     -> id_etage int,
#     -> capacite int);
# Query OK, 0 rows affected (0.01 sec)

# mysql> show tables;
# +------------------------+
# | Tables_in_laplateforme |
# +------------------------+
# | etage                  |
# | etudiants              |
# | salles                 |
# +------------------------+
# 3 rows in set (0.00 sec)