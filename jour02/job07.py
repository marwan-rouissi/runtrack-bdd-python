# import le module connector de mysql
import mysql.connector

# ma base de donnee
bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Bl@ckbird772",
    database = "job07"
)

# création d'un curseur
cursor = bd.cursor(buffered=True)

# 2e curseur
cursor2 = bd.cursor(buffered=True)

# mes requêtes
req = "SELECT * FROM employes where salaire > 3000;"
req2 = "select * from employes inner join services on employes.id_service = services.id;"

# execution de ma 1er requête
cursor.execute(req)

# execution de ma 2nde requête
cursor2.execute(req2)

# récupération de mes données
data = cursor.fetchall()
data2 = cursor2.fetchall()

# print de mes données
print("----------------------------------------------------------------------------------")
print(f"Les employés ayant un salaire suppérieur à 3000 euro: \n{data}")
# fermeture du curseur (par convention)
# cursor.close()
print("----------------------------------------------------------------------------------")
print(f"Les employés et leur service respectif: \n{data2}")
print("----------------------------------------------------------------------------------")

# fermeture du curseur (par convention)
cursor.close()