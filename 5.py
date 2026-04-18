from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np 

df = pd.read_csv('Titanic.csv')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna('S')
df=df.drop(columns='Cabin')
'''''''''
df['Sex'] = (df['Sex'] == 'female').astype(int)
X = df[['Age', 'Fare', 'Pclass', 'Sex']]
y = df['Survived']
# 80% for training, 20% for testing
# random_state=42 means same split every time you run it


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {round(accuracy * 100,1)}%")
'''
X = df[['Age', 'Fare', 'Pclass', 'Sex']]
y=df['Survived']
df['Sex'] = (df['Sex'] == 'female').astype(int)
df['Sex'] = (df['Sex'] == 'male').astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
passangers = pd.DataFrame({
    'Age' : [25],
    'Fare' : [100],
    'Pclass' : [1],
    'Sex' : [1]
})

prediciton = model.predict(passangers)
probability = model.predict_proba(passangers)

print(f"Survived :{'yes' if prediciton[0] ==1 else 'No'}")
print(f"probability :{round(probability[0][1] *100,1)}")

