# Travail en binôme

## Par

cordeiro maxime et echarif chefchaouni hicham

## Spécification technique

- Les frameworks à utiliser : Beautifulsoup, Selenium ou Scrapy.
- Nomenclature du dossier : nom1-prénom1_nom2-prénom2 à déposer dans le dossier suivant.
- Le projet doit être contenu dans un fichier app.py.
- Un fichier utiles.py contenant l’ensemble des class peut également être fourni.
- L'exécution du fichier app.py renvoie un fichier ‘.csv’ ou ‘json’ de 200 lignes ou met à jour le fichier préexistant.
- Les données sont également stockées dans une base de données.
- Le pipeline de collecte/transformation des données est entièrement rédigé à l’intérieur de fonctions ou de class.
- L'exécution de l’application prend en compte les arguments passés en ligne de commande.
- La collecte de données gère les exceptions.
- Le programme est fonctionnel et hébergé sur Github, le projet a reçu au moins 3 commits (un par membre de l’équipe).
- Une liste-compréhension est présente dans le programme et un f-string.

## Installer les dépendances nécéssaires

```python
pip install -r requirements.txt
```

## commande pour le script

python `app.py` `code postal`

Exemple:  

```bash
python app.py 91300
```

