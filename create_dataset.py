from os import listdir
import random
import os
import shutil

if __name__ == '__main__':
   path = "./Dataset_FR"

   pokemons = [p for p in listdir(path)]
   pokemon_oh = {}
   pokemon_classes = []

   if not os.path.isdir("Dataset_Yolo/"):
      os.mkdir(path + "/../Dataset_Yolo")
      os.mkdir(path + "/../Dataset_Yolo/train")
      os.mkdir(path + "/../Dataset_Yolo/val")

   current = 0
   for poke in pokemons:
      if not os.path.isdir("Dataset_Yolo/train/" +poke):
         os.mkdir(path + "/../Dataset_Yolo/train/" + poke)
         os.mkdir(path + "/../Dataset_Yolo/val/" + poke)
      images = [i for i in listdir(path + "/" + poke)]
      random.shuffle(images)
      size = len(images)
      train_nb = int(size * 0.9)
      for i in range(train_nb):
         shutil.copy(path + "/" + poke + "/" + images[i], path + "/../Dataset_Yolo/train/" + poke + "/" + images[i])
      for i in range(train_nb, len(images)):
         shutil.copy(path + "/" + poke + "/" + images[i], path + "/../Dataset_Yolo/val/" + poke + "/" + images[i])
      pokemon_oh[poke] = current
      pokemon_classes.append(poke)
      current += 1