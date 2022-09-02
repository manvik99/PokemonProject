from importlib.machinery import WindowsRegistryFinder
from unicodedata import name
from DataPreparation import prepareData
from pokemonClassification import pokemonClassification

if __name__ =='__main__':
    # prepareData() // To prepare the DataSet and store it as a csv file.
    
    [obese, overweight, healthy, underweight] = pokemonClassification() # classify the different pokemons into various groups

    while(True):
        name = (input("Enter pokemon name to access its Fitness Profile or STOP to exit:\n")).lower()
        if(name.upper() == 'STOP'):
            break
        
        exercise = ''
        fitnessLevel = ''
        remarks = ''
        if(name in obese):
            exercise += 'Slow Walking/ Swimming'
            fitnessLevel += 'Obese'
            remarks += 'You need to work hard towards a healthier lifestyle!'
        elif(name in overweight):
            exercise += 'Fast Walking/ Mild Sports'
            fitnessLevel += 'Overweight'
            remarks += 'Lets get fit!'
        elif(name in healthy):
            exercise += 'Running/ Sports/ Mountain Climbing'
            fitnessLevel += 'Healthy'
            remarks += 'Keep it up, being healthy is a journey!'
        elif(name in underweight):
            exercise += 'Weight Training'
            fitnessLevel += 'Underweight'
            remarks += 'Lets gain some weight!'
        else:
            print('Enter Valid Input')
            continue
        
        print('Pokemon Name: {name}\nFitness Level: {fitnessLevel}\nExercises Suggested: {exercise}\nRemarks: {remarks}\n'.format(name=name, fitnessLevel=fitnessLevel, exercise=exercise, remarks=remarks))
    
    
    
    # Some experimentation to try to display image to the console, failed, image is too pixalaed to be understood (Learnt that console works by using blocks)

    # response = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/22.png")
    # file = open("sample_image.png", "wb")
    # file.write(response.content)
    # file.close()j
    # output = climage.convert("sample_image.png", width=20)
    # # prints output on console.
    # print(output)





