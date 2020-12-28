import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# pokemon by types : Grass,Fire,Water,Poison
#print(df[df['Type 1'].isin(['Grass'])])
grass= df.loc[df['Type 1']=="Grass"]

# the top five attacked pockemon
attacked=df.sort_values('Attack',ascending=False).head(5)

#the top five fast pockemon
fast=df.sort_values('Speed',ascending=False).head(5).reset_index(drop=True).drop(columns=['#'])
attacked=df.sort_values('Attack',ascending=False).head(5).reset_index(drop=True).drop(columns=['#'])

# all the legendary pockemon
legendary = df.loc[df['Legendary']==True].reset_index(drop=True).drop(columns=['#']).head(50)

#how to drop columns : df.drop(columns=['#'])
grass = grass.reset_index(drop=True)
print(grass)
