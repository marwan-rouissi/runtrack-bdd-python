# import le module connector de mysql
import mysql.connector

# ma base de donnee
bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Bl@ckbird772",
    database = "laplateforme"
)

# création d'un curseur
cursor = bd.cursor()

# ma requête
req = "SELECT nom, capacite FROM salles"

# execution de ma requête
cursor.execute(req)

# récupération de mes données
data = cursor.fetchall()

# print de mes données
print(data)

# fermeture du curseur (par convention)
cursor.close()