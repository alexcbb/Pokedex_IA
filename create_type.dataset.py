import os
from os import listdir
import json
import shutil
import random
  
if __name__ == '__main__':
    path = "."

    f = open(path+"\\types.json")

    data = json.load(f)

    # Extraction de tout les types de Pokémons
    type_list = []
    for _, v in data.items():
        for type_pok in v:
            if type_pok not in type_list:
                type_list.append(type_pok)

    if not os.path.isdir("Type_Dataset/"):
        os.mkdir(path + "/Type_Dataset")
        os.mkdir(path + "/Type_Dataset/train")
        os.mkdir(path + "/Type_Dataset/val")

    # Création des fichiers de types
    for type_pok in type_list:
        if not os.path.isdir("Type_Dataset/train/" + type_pok):
            os.mkdir(path + "/Type_Dataset/train/" + type_pok)
            os.mkdir(path + "/Type_Dataset/val/" + type_pok)

    train = []
    val = []
    # Déplacement des images dans les dossiers
    for poke, v in data.items():
        for type_pok in v:
            images = [p for p in listdir(path+f"\\Dataset\\{poke}")]
            random.shuffle(images)
            size = len(images)
            train_nb = int(size * 0.9)
            for i in range(train_nb):
                shutil.copy(path+f"\\Dataset\\{poke}\\{images[i]}", path+f"\\Type_Dataset\\train\\{type_pok}\\{images[i]}")
            for i in range(train_nb, size):
                shutil.copy(path+f"\\Dataset\\{poke}\\{images[i]}", path+f"\\Type_Dataset\\val\\{type_pok}\\{images[i]}")
            

    f.close()