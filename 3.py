import pandas as pd
'''''
data = {
    'name' : ['Sebastian', 'Alice', 'Bob', 'Marek'],
    'age' : [25,24,23,22],
    'score' : [50,55,60,65],
    'city' : ['Łódź', 'Warsaw', 'Krakow', 'Gdańsk']
}

df=pd.DataFrame(data)
print(df)
df.head() # first 5 rows

df.tail() # last 5 rows

print(df.columns) # columns name
print(df.describe()) #statistics for number columns

print(df['name']) # selecting specific columns
print(df[df['score']>60]) # specific parameters

df['passed']=df['score']>55 # adding condition


print(df.sort_values('score',ascending=False)) #sorting

data_1= { 'name' : ['Sebastian', 'Alice', 'Bob', 'Marek'],
    'age' : [25,24,23,22],
    'score' : [50,55,60,75],
    'city' : ['Łódź', 'Warsaw', 'Krakow', 'Gdańsk']}

df=pd.DataFrame(data_1)
print(df)
print(df[['name', 'score']])
print(df[df['score']>70])
df['grade']=df['score'].apply(lambda x: 'pass' if x>=60 else 'fail') #adding column with a condition
print(df)

tt=pd.read_csv('titanic.csv')
print(tt.head())
print(tt.shape)
print(round(tt['Age'].mean(),2))
print(tt[tt['Age']>60])
print(round(tt['Fare'].mean(),2))
print(tt['Survived'].sum())
print(tt['Survived'].value_counts())# counting unique values
print(tt.groupby('Sex')['Age'].mean()) #grouping
print(tt.groupby('Pclass')['Survived'].mean())
print(tt['Sex'].value_counts())
print(tt.groupby('Pclass')['Age'].mean())


#tt=tt.dropna()
tt.drop(columns=['Cabin'],inplace=True)
#tt['Age'].fillna(tt['Age'].mean(),inplace=True)
#tt['Embarked'].fillna('S') # fill with most common value
#print(tt.isnull().sum())
'''

#1)
tc = pd.read_csv('titanic.csv')
tc = tc.dropna()
tc.drop(columns=['Cabin'],inplace=True)
tc['Age'].fillna(tc['Age'].mean(),inplace=True)
tc['Embarked'].fillna('S')
print(tc.isnull().sum())

#2)
print('Passangers:',tc.shape[0])
print(tc['Survived'].value_counts())
print(round(tc.groupby('Survived')['Age'].mean(),2))

#3)
print(round(tc.groupby('Sex')['Survived'].mean(),2))
print(round(tc.groupby('Pclass')['Survived'].mean(),2))
print(round(tc.groupby('Pclass')['Fare'].mean(),2))

#4)
tc['age_group'] = tc['Age'].apply(lambda x: 'child' if x < 18 else ('senior' if x>=60 else 'adult'))
tc['fare_level'] = tc['Fare'].apply(lambda x: 'low' if x < 50 else ('high' if x>=100 else 'medium'))

#5)
print(round(tc.groupby('age_group')['Survived'].mean(),2))

#newer Pandas prefers tc['Age'] = tc['Age'].fillna(...) over inplace=True.
#Y tc = tc.dropna() BEFORE filling missing values — so it dropped all 708 rows with any missing data first, leaving only 183 passengers instead of 891
