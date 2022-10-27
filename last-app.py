# Import du package sqlalchemy permetant de gérer les bases de données
import sqlalchemy as db

# Import de la class DataBase permettant de créer des bases de données
from utils import DataBase

# Instaciation de la base de données 'tenup.sqlite'
database_name = "tenup"
table_name = "tournois"
base = DataBase(database_name)

# Création d'une table nommée "tournois" dans la base de données 'tenup.sqlite'
base.create_table(table_name, 
                 name=db.String, # nom du tournois
                 location=db.String, # - la localisation du tournois
                 start_date=db.String, # date de début        
                 end_date=db.String, # date de fin
                 category=db.String, # catégorie des participants
                 distance=db.String, # la disctance par rapport au point de recherche
                 search_location=db.String, # le point de recherche
                 search_time=db.String # la date et l'heure de la recherche
                 )

# Création d'un objet item contenant les données à stocker dans la base de données
item = {}
item['name'] = "test"
item['location'] = "paris"
item['start_date'] = "27/10/22"
item['end_date'] = "27/10/22"
item['category'] = "MS"
item['distance'] = "2,7"
item['search_location'] = "Massy, 91, Essonne, Île-de-France"
item['search_time'] = "27/10/22"
print(item)

# Ajout d'une ligne dans la base de données 'tenup.sqlite'
base.add_row(table_name,
                 name=item['name'], # nom du tournois
                 location=item['location'], # - la localisation du tournois
                 start_date=item['start_date'], # date de début        
                 end_date=item['end_date'], # date de fin
                 category=item['category'], # catégorie des participants
                 distance=item['distance'], # la disctance par rapport au point de recherche
                 search_location=item['search_location'], # le point de recherche
                 search_time=item['search_time'] # la date et l'heure de la recherche
            )


# Afficher les colonnes de la table
data_read = base.read_table(table_name)
print(data_read)
print(data_read.columns.keys())

# Afficher le contenu de la table 'Table_Test'
print(base.select_table(table_name))