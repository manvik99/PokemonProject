# Pokemon Fitness Profile
Using PokeAPI dataset, lets try to find fitness levels of various pokemons and suggest appropriate exercises!

## Category: Senior 

I've been writing code for about 20 months

### Quick Start

To run the project follow the steps below:

1) Create a virtual env and install the dependencies using pip install -r requirements.txt
2) Run the command: python .\main.py
3) Enter the pokemon Name and get access to its fitness profile and suggested workout plans

### Project Overview

The code flow is explained breifly in the steps below:

1) First we get the names of pokemons(say 500) and then using /pokemon/{name} we get access to its profile.
2) We store its weight, height and then calculate its BMI.
3) We also store its 'type' is another table. Its stored in another table as its 1:m relation, thus we need to normalise the table.
4) We sort the dataframe using BMI as the key, do some analytics( check out Analysis.ipynb ) such as line grapb of BMI's and boxplot to get the mean and outliers.
5) Using some basic filters we categorize the pokemon into obese, overweight, healthy or underweight.
6) We encourage the pokemons to adopt healthier lifestyle.

### Sample I/O

Enter pokemon name to access its Fitness Profile or STOP to exit: <br />
snorlax <br />
Pokemon Name: snorlax <br />
Fitness Level: Obese <br />
Exercises Suggested: Slow Walking/ Swimming <br />
Remarks: You need to work hard towards a healthier lifestyle! <br />

Enter pokemon name to access its Fitness Profile or STOP to exit: <br />
pikachu <br />
Pokemon Name: pikachu <br />
Fitness Level: Healthy <br />
Exercises Suggested: Running/ Sports/ Mountain Climbing <br />
Remarks: Keep it up, being healthy is a journey! <br />

### Future Scope

We can continue the development of this project using some pointers below:

1) Add a diet plan using the /berry/{id or name}/ endpoint to suggest proper diet to various pokemons!
2) Have multiple fitness events organised and invite all the appropriate pokemons to it!
