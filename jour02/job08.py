# import le module connector de mysql
import mysql.connector

class Zoo:

    def __init__(self) -> None:

        # ma base de donnee
        self.bd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Bl@ckbird772",
            database = "zoo"
        )

        # création d'un curseur
        self.cursor = self.bd.cursor()

    def AjouterAnimal(self, nom, race, id_cage, date_naissance, pays_origine):
        # requête
        req = f"""insert into animal (nom, race, id_cage, date_naissance, pays_origine) \
            values \
            ('{nom}', '{race}', {id_cage}, '{date_naissance}', '{pays_origine}');"""

        # execution de ma requête
        self.cursor.execute(req)
  
        # fermeture du curseur (par convention)
        self.cursor.close()
        print(req)

    def SupprimerAnimal(self, nom):
        # requête
        req = f"delete from zoo where nom = {nom}"

        # execution de ma requête
        self.cursor.execute(req)
  
        # fermeture du curseur (par convention)
        self.cursor.close()
    
    def ModifierAnimal(self):
        pass

    def AjouterCage(self, superficie, capacité):
        # requête
        req = f"insert into animal (id, nom, race, id_cage, date_naissance, pays_origine) \
            values \
                ('{superficie}', '{capacité}');"

        # execution de ma requête
        self.cursor.execute(req)
  
        # fermeture du curseur (par convention)
        self.cursor.close()

    def SupprimerCage(self, id):
        # requête
        req = f"delete from zoo where id = {id}"

        # execution de ma requête
        self.cursor.execute(req)
  
        # fermeture du curseur (par convention)
        self.cursor.close()

    def ModifierCage(self):
        pass

    def AfficherZoo(self):
        # requête
        req1 = f"select * from animal"
        
        # execution de ma requête
        self.cursor.execute(req1)
        # récupération de mes données
        self.data = self.cursor.fetchall()
        print(f"L'ensemble des animaux présents dans le zoo:\n{self.data}")
        # fermeture du curseur (par convention)
        self.cursor.close()

    def AfficherAnimauxEnCages(self):
        # requête
        req2 = f"select * from animal inner join cage on animal.id_cage = cage.id;"

        # execution de ma requête
        self.cursor.execute(req2)
        # récupération de mes données
        self.data2 = self.cursor.fetchall()
        print(f"Les animaux présents dans les cages:\n{self.data2}")
        # fermeture du curseur (par convention)
        self.cursor.close()
    
    def AfficherSuperficieCages(self):
        # requête
        req3 = f"SELECT sum(superficie) FROM cage"

        # execution de ma requête
        self.cursor.execute(req3)
        # récupération de mes données
        self.data3 = self.cursor.fetchall()
        # print de mes données
        print(f"La superficie totale de toutes les cages est de: {self.data3[0]} m2")
        # fermeture du curseur (par convention)
        self.cursor.close()


# animal (id, nom, race, id_cage, date_naissance, pays_origine)

# cage (id, superficie, capacité)

# print("Que voulez vous faire mr. le directeur ?")
# print("ajouter / supprimer / modifier")


# terminer les methodes manquantes
# créer la bd zoo et ses tables animal et cage
# peupler le zoo

zoo = Zoo()

# zoo.AjouterAnimal("Léo", "lion", 1, "20-08-2020", "Sénégal")
zoo.AfficherZoo()