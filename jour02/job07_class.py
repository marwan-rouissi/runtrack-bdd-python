# import le module connector de mysql
import mysql.connector

class CRUD:

    def __init__(self) -> None:
        # ma base de donnee
        self.bd = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Bl@ckbird772",
            database = "job07"
        )
        # # création d'un curseur
        # self.cursor = self.bd.cursor(buffered=True)

    # créer une nouvelle colonne
    def create(self, nomTable, nomColonne, typeColonne):
        req = f"alter table {nomTable} \
            add {nomColonne} {typeColonne}"

        # création d'un curseur
        self.cursorCreate = self.bd.cursor(buffered=True)

        # execution de ma requête
        self.cursorCreate.execute(req)
  
        # fermeture du curseur (par convention)
        self.cursorCreate.close()
    
    # 
    def read(self, element, table):
        # ma requête
        req = f"select {element} from {table};"

        # création d'un curseur
        self.cursorRead = self.bd.cursor(buffered=True)

        # execution de ma requête
        self.cursorRead.execute(req)

        # récupération de mes données
        self.dataRead = self.cursorRead.fetchall()

        # Imprimer le resultat
        print(self.dataRead)

        # fermeture du curseur (par convention)
        self.cursorRead.close()

    def update(self, table, element, typeColonne):
        # ma requête 
        req = f"alter table {table} \
            modify {element} {typeColonne}"

        # création d'un curseur
        self.cursorUpdate = self.bd.cursor(buffered=True)

        # execution de ma requête
        self.cursorUpdate.execute(req)

        # récupération de mes données
        self.dataUpdate = self.cursorUpdate.fetchone()

        # fermeture du curseur (par convention)
        self.cursorUpdate.close()


    def delete(self, element, table):
        # ma requête
        req = f"alter table {table} \
            drop {element}"

        # création d'un curseur
        self.cursorDelete = self.bd.cursor(buffered=True)

        # execution de ma requête
        self.cursorDelete.execute(req)

        # récupération de mes données
        self.dataDel = self.cursorDelete.fetchone()

        # fermeture du curseur (par convention)
        self.cursorDelete.close()

bdd = CRUD()
bdd.create("employes" ,"test", "varchar(255)")
print("----------------------------------------------------------------------------------")
bdd.read("*", "employes")
print("----------------------------------------------------------------------------------")
# bdd.update("employes", "test", "decimal")
# bdd.delete("test", "employes")