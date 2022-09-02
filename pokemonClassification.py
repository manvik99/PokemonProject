import pandas as pd

def pokemonClassification():
    pokemonBasicData = pd.read_csv("./pokemonBasicData")
    pokemonType = pd.read_csv("./pokemonType")
    obese = []
    overweight = []
    healthy = []
    underweight = []
    
    for index, row in pokemonBasicData.iterrows():
        name = row['Name']
        bmi = row['BMI']
        types = list((pokemonType.loc[pokemonType['Name'] == name])['Type'])
        
        isSteelOrRock = ('steel' in types) or ('rock' in types) # Assuming pokemons made of steel or rock and healthy

        if(bmi >= 10 and (not isSteelOrRock)): # obese pokemons
            obese.append(name)
        elif(bmi >=4 and bmi < 10 and (not isSteelOrRock)): # overweight pokemons
            overweight.append(name)
        elif(bmi >= 2 and bmi < 4 or isSteelOrRock): # healthy pokemons
            healthy.append(name)
        else:
            underweight.append(name) # underweight pokemons
    return [obese, overweight, healthy, underweight]