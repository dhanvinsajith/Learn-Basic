import pandas as pd
import re


#READING DIFFERENT FILES
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
'''
print(pokemonCsv.columns)
print(pokemonCsv['Name'][:50]) #prints first 50 in name column
print(pokemonCsv[['Name', 'HP', 'Generation']][50:100]) #given columns of pokemon 50 to 99
print(pokemonCsv.iloc[1:10]) #gives rows 1 to 9
print(pokemonCsv.iloc[2, 1]) #gives item on 2nd row, 1st column iloc[R, C]
print(pokemonCsv.iloc[2:7, 1])
for index, row in pokemonCsv.iterrows():
    print(index, row['Name'])
print(pokemonCsv.loc[pokemonCsv['Legendary'] == 1]) #prints all legendary pokemon
print(pokemonCsv.loc[pokemonCsv['Type 1'] == "Fire"]) #prints all fire type pokemon
print(pokemonCsv.describe()) #gives statistical info of each column
print(pokemonCsv.sort_values('Name', ascending = False)) #reverse alphabetical order
print(pokemonCsv.sort_values(['Type 1', 'HP'])) #sorts alphabetically by 'Type 1' column first then ascending in 'HP' column
print(pokemonCsv.sort_values(['Attack', 'HP'], ascending = [0, 1])) #checks attack descending and health ascending
'''


#MAKING CHANGES
'''
pokemonCsv['Total'] = pokemonCsv['HP'] + pokemonCsv['Attack'] + pokemonCsv['Defense'] + pokemonCsv['Sp. Atk'] + pokemonCsv['Sp. Def'] + pokemonCsv['Speed'] #method one of adding a column
pokemonCsv = pokemonCsv.drop(columns = ['Total']) #removing a specific column
pokemonCsv['Total'] = pokemonCsv.iloc[:, 4:10].sum(axis = 1) #axis = 1 means horizontal and axis = 0 is vertical
cols = list(pokemonCsv.columns.values) #getting columns in list
pokemonCsv = pokemonCsv[cols[0:10] + [cols[-1]] + cols[10:12]] #changing position of column 'total'
print(pokemonCsv)
'''


#SAVING CSV
'''
#modifying
pokemonCsv['Total'] = pokemonCsv.iloc[:, 4:10].sum(axis = 1)
cols = list(pokemonCsv.columns.values)
pokemonCsv = pokemonCsv[cols[0:10] + [cols[-1]] + cols[10:12]]

#saving
pokemonCsv.to_csv('modified.csv', index = False)
pokemonCsv.to_excel('modified.xlsx', index = False)
pokemonCsv.to_csv('modified.txt', index = False, sep = '\t')
'''


#FILTERING DATA
#Common question: Difference between loc and iloc. Answer: the i in iloc stands for integer. loc filters rows and columns based on label names while iloc filters rows and columns based on integer values
'''
print(pokemonCsv.loc[(pokemonCsv['Legendary'] == 1) & (pokemonCsv["Type 1"] == "Fire")]) #prints all pokemon who are fire type AND legendary
print(pokemonCsv.loc[((pokemonCsv["Type 1"] == "Water") | (pokemonCsv["Type 1"] == "Fire")) & (pokemonCsv['Legendary'] == 1)]) #prints all fire OR water type1 pokemon which are legendary
filtered_data = pokemonCsv.loc[((pokemonCsv["Type 1"] == "Water") | (pokemonCsv["Type 1"] == "Fire")) & (pokemonCsv['Legendary'] == 1)]
filtered_data.reset_index(drop = True, inplace = True) #resetting index values from old csv
print(filtered_data)
print(pokemonCsv.loc[pokemonCsv['Name'].str.contains('Mega')]) #every pokemon with Mega in its name
print(pokemonCsv.loc[~pokemonCsv['Name'].str.contains('Mega')]) #every pokemon without Mega in its name
print(pokemonCsv.loc[pokemonCsv['Type 1'].str.contains('Fire|Water', regex = True)]) #printing all fire and water type1 pokemon with re (regular expressions)
print(pokemonCsv.loc[pokemonCsv['Type 1'].str.contains('fire|water', flags = re.I, regex = True)]) #flags = re.I means it will ignore capitalization
print(pokemonCsv.loc[pokemonCsv['Name'].str.contains('^pi[a-z]*', flags = re.I, regex = True)]) #all pokemon names beginning with 'pi'
'''


#CONDITIONAL CHANGES
'''
pokemonCsv.loc[pokemonCsv['Type 1'] == 'Water', 'Type 1'] = 'Wet' #changed 'Water' type to 'Wet' type pokemon
pokemonCsv.loc[pokemonCsv['Type 1'] == 'Electric', 'Legendary'] = True #changed all electric types to legendary = True
pokemonCsv.loc[pokemonCsv['HP'] > 60, ['Generation', 'Legendary']] = [50, True] #changes two values if hp > 60
print(pokemonCsv[100:150])
'''


#STATISTICS
'''
print(pokemonCsv.groupby(['Type 1']).mean()) #average statistics of each type of pokemon
print(pokemonCsv.groupby(['Type 1']).mean().sort_values('HP', ascending = False)) #sorts by average HP in descending order for each Type1
print(pokemonCsv.groupby(['Type 1']).sum()) #doesnt make sense for pokemon but useful in other cases
pokemonCsv['count'] = 1 #creating column to make count easier
print(pokemonCsv.groupby(['Type 1']).count()['count']) #using count column to find count
print(pokemonCsv.groupby(['Type 1', 'Type 2']).count()['count']) #subcategories of each Type1
'''


#LARGE AMOUNTS OF DATA
'''
for df in pd.read_csv('pokemon_data.csv', chunksize = 5): #5 rows are being passed at a time
    print("CHUNK")
    print(df)

tf = pd.read_csv('pokemon_data.csv')
new_tf = pd.DataFrame(columns = tf.columns)
for tf in pd.read_csv('pokemon_data.csv', chunksize = 5):
    results = tf.groupby(['Type 1'].count())
    new_tf = pd.concat([new_tf, results])
'''