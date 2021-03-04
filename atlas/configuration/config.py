# -*- coding:utf-8 -*-

# Connexion de l'application à la BDD
# Remplacer user, monpassachanger, IPADRESSE (localhost si la BDD est sur le même serveur que l'application), 
# eventuellement le port de la BDD et le nom de la BDD avec l'utilisateur qui a des droits de lecture sur les vues de l'atlas (user_pg dans settings.ini)
database_connection = "postgresql://geonatatlas:h6nHUh_7!P7M@localhost:63333/geonatureatlas"

#################################
#################################
### Customisation application ###
#################################
#################################

# Nom de la structure
STRUCTURE = "Nom de la structure"

# Nom de l'application
NOM_APPLICATION = "Biodiv'Rennes"

# URL de l'application depuis la racine du domaine
# ex "/atlas" pour une URL: http://mon-domaine/atlas OU "" si l'application est accessible à la racine du domaine
URL_APPLICATION = "/atlas"

###########################
###### Cartographie #######
###########################

# Configuration des cartes (centre du territoire, couches CARTE et ORTHO, échelle par défaut...)
MAP = {
    'LAT_LONG': [48.11351870299793, -1.666504010306364],
    'FIRST_MAP': {
        'url': 'https://public.sig.rennesmetropole.fr/geowebcache/service/wmts?LAYER=ref_fonds:pvci&FORMAT=image/png&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=EPSG:3857&TILEMATRIX=EPSG:3857:{z}&TILEROW={y}&TILECOL={x}',
        'attribution': '&copy rennesmetropole.fr',
        'tileName': 'Plan de ville couleur',
    },
'SECOND_MAP' : {'url':'https://public.sig.rennesmetropole.fr/geowebcache/service/wmts?LAYER=raster:ortho2017&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=EPSG:3857&TILEMATRIX=EPSG:3857:{z}&TILEROW={y}&TILECOL={x}',
                'attribution': '&copy rennesmetropole.fr',
                'tileName': 'Orthophotographie 2017'
},
'ZOOM' : 13,
# Pas du slider sur les annees d'observations: 1 = pas de 1 an sur le slider
'STEP': 1,
# Couleur et épaisseur des limites du territoire
'BORDERS_COLOR': '#000000',
'BORDERS_WEIGHT': 3,
'ENABLE_SLIDER': True

}

# Permet de lister les pages statiques souhaitées et de les afficher dynamiquement dans le menu sidebar
# Les pictos se limitent au Glyphicon proposés par Bootstrap (https://getbootstrap.com/docs/3.3/components/)

STATIC_PAGES = {
    'presentation': {'title': "Présentation de l'atlas", 'picto': 'glyphicon-question-sign', 'order': 0, 'template': 'static/custom/templates/presentation.html'},
    'partenaires': {'title': "Nos partenaires", 'picto': 'glyphicon-link', 'order': 1, 'template': 'static/custom/templates/partenaires.html'},
    'enquètes': {'title': "Enquètes Biodiv'Rennes", 'picto': 'glyphicon-search', 'order': 2, 'template': 'static/custom/templates/partenaires.html'}
}

# Affichage des observations par maille ou point
# True = maille / False = point
AFFICHAGE_MAILLE = True

# Niveau de zoom à partir duquel on passe à l'affichage en point (si AFFICHAGE_MAILLE = False)
ZOOM_LEVEL_POINT = 11

# Limite du  nombre d'observations à partir duquel on passe à l'affichage en cluster
LIMIT_CLUSTER_POINT = 1000

# Carte de la page d'accueil: observations des 'x' derniers jours. Bien mettre en anglais et non accordé
NB_DAY_LAST_OBS = '4000 day'
# Texte à afficher pour décrire la cartographie des 'dernières observations'
TEXT_LAST_OBS = 'Les dernières observations enregistrées |'

# Carte de la fiche commune: nombre des 'x' dernières observations affichées
NB_LAST_OBS=100

###########################
###### PAGE ACCUEIL #######
###########################


## BLOC STAT PAR RANG : Parametre pour le bloc statistique 2 de la page d'accueil (statistiques par rang remontant 2 espèces aléatoirement ayant au moins une photo)
# Ce bloc peut être affiché ou non et peut être affiché sur 2, 3 ou 4 colonnes. Il est ainsi possible de mettre autant de blocs que souhaité (2, 3, 4, 6, 8...)
# Mettre dans RANG_STAT le couple 'rang taxonomique' - 'nom du taxon correspondant au rang' pour avoir des statistique sur ce rang -
# Fonctionne à tous les niveaux de rang présents dans la table taxref -

RANG_STAT = [{'phylum': ["Chordata"]}, {'phylum': ["Chordata"]}]
RANG_STAT_FR = ['Faune vertébrée', 'Faune vertébrée']

#RANG_STAT = [{'phylum': ["Arthropoda", "Mollusca", "Annelida", "Cnidaria", "Platyhelminthes"]}, {'phylum': ["Chordata"]}, {'regne': ["Plantae"]}]
#RANG_STAT_FR = ['Faune invertébrée', 'Faune vertébrée', 'Flore']

AFFICHAGE_RANG_STAT = True

# Bloc avec espèces à voir en ce moment. Affichage True/False
AFFICHAGE_EN_CE_MOMENT = True

############################
####### FICHE ESPECE #######
############################

# Rang taxonomique qui fixe jusqu'à quel taxon remonte la filiation taxonomique (hierarchie dans la fiche d'identite : Famille, Ordre etc... )
LIMIT_RANG_TAXONOMIQUE_HIERARCHIE = 13

# Rang taxonomique qui fixe la limite de l'affichage de la fiche espece ou de la liste
# 35 = ESPECE
# On prend alors tout ce qui est inferieur ou egal a l'espece pour faire des fiches et ce qui est superieur pour les listes
LIMIT_FICHE_LISTE_HIERARCHY = 28

# URL d'accès aux photos et autres médias (URL racine). Par exemple l'url d'accès à Taxhub
# Cette url sera cachée aux utilisateurs de l'atlas
REMOTE_MEDIAS_URL = "http://abc-biodivrennes.fr/taxhub/"
# Racine du chemin des fichiers médias stockés dans le champ "chemin" de "atlas.vm_medias"
# Seule cette partie de l'url sera visible pour les utilisateurs de l'atlas
REMOTE_MEDIAS_PATH = "static/medias/"

# URL de TaxHub (pour génération à la volée des vignettes des images).
# Si le service Taxhub n'est pas utilisé, commenter la variable
REDIMENSIONNEMENT_IMAGE = False
# si redimmentionnement image = True, indiquer l'URL de taxhub
TAXHUB_URL = "http://abc-biodivrennes.fr/taxhub"

STAT = {"DISPLAY_CLASSE_ALTITUDE": False, "DISPLAY_OBS_MENSUELLE": True}