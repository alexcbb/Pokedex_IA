from os import listdir
import requests
import json

if __name__ == '__main__':
    # Accède à l'api de : https://api-pokemon-fr.vercel.app/
    api = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/"

    path_fr = "./Dataset_FR" 
    pokemons_fr = [p for p in listdir(path_fr)]
    map_poke_type = {}
    for i in range(len(pokemons_fr)):
        final_api = api+ pokemons_fr[i].lower()
        result = requests.get(final_api).json()
        poke_types = result['types']
        map_poke_type[pokemons_fr[i]] = []
        for type in poke_types:
            type_name = type['name']
            map_poke_type[pokemons_fr[i]].append(type_name.replace("\u00c9", "E").replace("\u00e9", "e"))
         
    json_object = json.dumps(map_poke_type, indent = 4) 
    with open("types.json", "w") as f:
        f.write(json_object)