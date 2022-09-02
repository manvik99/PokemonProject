import requests
import pandas as pd

def prepareData():

    # Get all pokemon names in the pokeAPI dataset

    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=500")
    data = response.json()
    pokemonNames = []
    for value in data['results']:
        pokemonNames.append(value['name'])

    #Normalising the tables, as it is 1:m relation between pokemon and its type.
  
    table_1 = []
    table_2 = []
    for name in pokemonNames:
        response = (requests.get("https://pokeapi.co/api/v2/pokemon/{name}".format(name = name))).json()
        height = response['height']
        weight = response['weight']
        bmi = round(response['weight']/(response['height'] * response['height']),2)
        table_1.append([name, height, weight, bmi])
        for field in response['types']:
            table_2.append([name, field['type']['name']])

    pokemonBasicData = pd.DataFrame(table_1, columns =['Name', 'Height', 'Weight', 'BMI']) 
    pokemonBasicData.sort_values('BMI',ascending=False ,inplace=True)
    pokemonType = pd.DataFrame(table_2, columns =['Name', 'Type']) 

    pokemonBasicData.to_csv('pokemonBasicData')
    pokemonType.to_csv('pokemonType')
