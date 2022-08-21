Projet 04 : Application gérant un tournoi d'échecs


Ce projet consiste à créer une application qui permet de créer la structure d'un tournoi d'échecs, qui permet d'ajouter des joueurs dans une base de données. Le programme utilise l'algorithme du tournoi suisse pour calculer la rotation des joueurs afin d'avoir des matchs équilibrés et d'éviter la répétition des matchs.

Ce projet est écrit dans le modèle de conception MVC - Modèles - Vues - Contrôleurs, et les données sont enregistrées dans la librairie de base de données TinyDB


Cette application permet de :
    Créez et enregistrez des joueurs.
    Mettre à jour les score des joueurs.
    Créez et enregistrez des tournois.
    Organisez des tournois.
    Reprendre un tournoi inachevé.

Conditions préalables

Commencez par installer Python en premier via https://www.python.org/downloads/ 

Création de l'environnement virtuel
python -m venv venv 

Activation de l'environnement virtuel :
Linux, Mac (à toi te me dire):
source venv/Scripts/activate

Windows:
venv\Scripts\activate.bat (cmd)
venv\Scripts\Activate.ps1 (poweshell)

Installation des dépendances
pip install -r requirements.txt

Installation Flake8:
pip install flake8

Pour générer un rapport flake8 HTML:
flake8 --format=html --htmldir=flake-report

Start:
Vous pouvez enfin lancer le script depuis un terminal via la commande :
python main.py

Rapport flake8:
Le projet contient un rapport flake8 sans erreur. Pour générer un rapport flake8, installez le module flake8.

Le fichier setup.cfg à la racine contient les paramètres concernant la génération du rapport.

Le rapport se trouve dans le fichier flake-report