# Pokédex Pokémon

Ce projet a été créé dans le cadre d'une vidéo Youtube de la chaîne [BeegBrain](https://www.youtube.com/@beegbrain).
L'objectif était de récréer le Pokédex à partir de modèles d'intelligence artificielle.

Afin d'utiliser ce projet veuillez suivre les instructions suivantes.

## Installation

### 1) Installer Conda + Créer environnement
#### Linux
- Télécharger [Miniconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers)
- Lancer la commande dans un terminal (là où est situé le fichier téléchargé): `bash ./Miniconda3-latest-Linux-x86_64.sh`
- Rédemarrer le terminal
- Lancer la commande `conda create --name EnvAI` puis compléter la création de l'environnement

#### Windows
- Installer [Anaconda](https://www.anaconda.com/download)
- Lancer le *Anaconda Navigator*
- Aller dans 'Environnements'
- Créer un environnement appelé 'EnvAI' en version de Python >= 3.10

### 2) Installer les dépendances
Après avoir installé puis activé l'environnement, l'idée est d'installer les dépendances nécessaires. 
L'idée est alors d'ouvrir un terminal (sur Windows ouvrir depuis le navigateur Anaconda) puis de lancer les commandes suivantes :
- `conda activate EnvAI`
- `pip install ultralytics`
- `pip install requests`

## Vue du code
Pour ce projet, j'ai utilisé une base de données contenant les noms et images des Pokémons de la première génération issue du site Kaggle : https://www.kaggle.com/datasets/thedagger/pokemon-generation-one. Le projet contient la base de données pré-traitée afin de pouvoir être utilisée avec le modèle entraîné : YOLOv8. J'ai laissé à disposition les scripts m'ayant permis de préparer les bases de données : `create_dataset.py` et `create_type_dataset.py`

Au final le projet dispose des dossiers de base de données suivants :
- `Dataset_EN` : la base de données originale (en Anglais)
- `Dataset_FR` : la base de données avec les noms des Pokémons en Français
- `Dataset_YOLO` : la base de données prête pour l'entrainement du modèle YOLO
- `Type_Dataset` : la base de données pour apprendre les types

La base de données originale ne contient pas les types des Pokémons. Afin de les obtenir, j'ai utilisé un script me permettant d'accéder à une API en ligne pour extraire les types de la première génération : `get_type.py`
Ce script vient contenir les informations extraites dans le fichier `types.json` qui est ensuite utilisé par `create_type_dataset.py` afin de créer la base de données `Type_Dataset`

Une fois les bases de données créées, il suffit de lancer l'entraînement du modèle de détection du Pokémon et de type avec les scripts : `train.py` et `train_type.py`.

Au final, le script `predict.py` permet d'extraire l'information souhaitée (nom ou type du Pokémon) en modifiant les informations intéressantes.

## Contact
Si ce projet vous plaît, soutenez moi en mettant une étoile sur Github et en allant donner un pouce bleu à la vidéo associée sur ma chaîne Youtube.

Pour toute question, contactez-moi au mail suivant : beegbraincontact@gmail.com.