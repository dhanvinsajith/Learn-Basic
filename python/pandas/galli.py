import pandas as pd

pokemonCsv = pd.read_csv('pokemon_data.csv')
pokemonXl = pd.read_excel('pokemon_data.xlsx')
pokemonTxt = pd.read_csv('pokemon_data.csv', delimiter = '\t')

#ACCESSING FILES
'''
print(pokemonCsv) #whole thing
print(pokemonTxt)
print(pokemonXl)
print(pokemonCsv.head(3)) #top 3 rows, by default 5
print(pokemonXl.tail(3)) #last 3 rows, by default 5
'''


#READING SPECIFICS
print(pokemonCsv.columns)