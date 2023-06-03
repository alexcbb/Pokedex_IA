# Librairies à importer
from ultralytics import YOLO

if __name__ == '__main__':
    path = "./dracau.jpg" # Chemin menant à l'image à tester

    model = YOLO('./classify_type.pt') # Modèle à utiliser, doit changer si on veuty le nom/type du Pokémon

    results = model.predict(path)
    # Utiliser ensuite https://docs.ultralytics.com/modes/predict/ afin d'extraire l'information intéressante

