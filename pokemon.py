from flask import *
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_csv('pokemon_data.csv') #if you want to open excel file you just have to do: pd.read_excel('name of the excel file')
    new_df = df.loc[df['Name'].str.contains('Mega')]
    return render_template('landing.html',table=new_df.to_html())

@app.route('/pokemonType',methods =('GET','POST'))
def typePokemon():
    df = pd.read_csv('pokemon_data.csv')
    grass= df.loc[df['Type 1']=="Grass"].head(5).reset_index(drop=True).drop(columns=['#','Type 1','Type 2'])
    fire = df.loc[df['Type 1']=="Fire"].head(5).reset_index(drop=True).drop(columns=['#','Type 1','Type 2'])
    water = df.loc[df['Type 1']=="Water"].head(5).reset_index(drop=True).drop(columns=['#','Type 1','Type 2'])
    poison = df.loc[df['Type 1']=="Poison"].head(5).reset_index(drop=True).drop(columns=['#','Type 1','Type 2'])
    return render_template('typePokemon.html',tables=[fire.to_html(classes='fire'), water.to_html(classes='water'),poison.to_html(classes='poison'),grass.to_html(classes='grass')],titles = ['na','Fire Pokemon', 'Water Pokemon','Poison Pokemon','Grass Pokemon'], icones= ["fa-fire","fa-fire","fa-tint","fa-skull-crossbones"], classesTitles=["index","fire-pokemon","water-pokemon","poison-pokemon","grass-pokemon"])

@app.route('/topfive',methods=('GET','POST'))
def topfive():
    df = pd.read_csv('pokemon_data.csv')
    fast=df.sort_values('Speed',ascending=False).head(5).reset_index(drop=True).drop(columns=['#'])
    attacked=df.sort_values('Attack',ascending=False).head(5).reset_index(drop=True).drop(columns=['#'])
    return render_template('topfive.html',tables=[fast.to_html(classes='fastest'),attacked.to_html(classes='attacked')],titles=["","Top five fastest Pokémon","Top five attacker Pokémon"])

@app.route('/legendary',methods=('GET','POST'))
def legendaryPokemon():
    df = pd.read_csv('pokemon_data.csv')
    legendary = df.loc[df['Legendary']==True].reset_index(drop=True).drop(columns=['#']).head(50)
    return render_template('legendary.html',table=legendary.to_html())
## Read Headers
#print(df)
#read each column
#print(df['Name'][0:5])

#read each row
#print(df.iloc[0:4])
#print(df.loc[df['Type 1']=="Fire"])
#print(df.describe())
#print(df.sort_values('Type 1'))
#print(df.loc[(df['Type 1']=='Grass') & (df['Type 2'] =='Poison')])
#new_df.to_excel('modified.xlsx',index=False) // how to save it to excel
#print(df.groupby(['Type 1']).mean())
if __name__ == '__main__':
    app.run(debug=True)
