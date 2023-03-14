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
req = "SELECT sum(superficie) FROM etage"

# execution de ma requête
cursor.execute(req)

# récupération de mes données
data = cursor.fetchone()

# print de mes données
print(f"La superficie de La Plateforme est de {data[0]} m2")

# fermeture du curseur (par convention)
cursor.close()