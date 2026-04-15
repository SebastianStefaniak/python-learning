import pandas as pd 
import numpy as np 
from scipy import stats
'''''
ages = np.array([10,12,14,25,38,55])
mean = np.mean(ages)
print(mean)
median = np.median(ages)
print(median)
std = np.std(ages)
print(std) #how spread out the data is
variance = np.var(ages)# same but it's harder to interpret because of unit squared
print(variance)
'''
'''''
df=pd.DataFrame({
    'study hours' : [2,4,6,8,10],
    'score' : [45,60,70,85,100]
})

print(df.corr())
'''

'''''
ages = np.array([10,12,14,25,38,55])
Q1 = np.percentile(ages,25)
Q3 = np.percentile(ages, 75)
IQR = Q3-Q1

lower = Q1 - 1.5 * IQR # detecting outlier values
upper = Q3 + 1.5 * IQR 
outliers=ages[(ages<lower) | (ages>upper)]
print(outliers)

df=pd.read_csv('titanic.csv')
mean=np.mean(df['Age'])
median=np.median(df['Age'])
std=np.std(df['Age'])
print(f"mean is: {mean}, Median is: {median}, std is: {std}")
print(df[['Age', 'Fare', 'Survived']].corr())
Q1 = np.percentile(df['Fare'],25)
Q3 = np.percentile(df['Fare'],75)
IQR =Q3 - Q1 
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outlier = df[(df['Fare'] < lower) | (df['Fare'] > upper)]
print(outlier)
'''


df=pd.read_csv('titanic.csv')
#Basic probability
total = len(df)
survived = df['Survived'].sum()
p_survival = survived / total
print(round(p_survival,2))
'''''
#conditional probability
women = df[df['Sex'] == 'female']
p_survival_women = women['Survived'].mean()
print(round(p_survival_women,2))

dice = np.random.randint(1, 7, size = 1000)
unique, counts = np.unique(dice, return_counts = True)
for val, cnt in zip(unique,counts):
    print(f"{val}: {cnt/100:.2f}")



ages = np.random.normal(loc=30, scale=10, size=1000) #loc=mean, scale=std
print(round(np.mean(ages),1))
print(round(np.std(ages),1))


flips = np.random.randint(0, 2, size=1000)
print(np.mean(flips))
'''''
'''''''''''
p_survived=df['Survived'].mean()
print(round(p_survived,2))

p_1class = df[df['Pclass'] == 1]['Survived'].mean()
p_3class = df[df['Pclass'] ==3]['Survived'].mean() 
child_s=df[df['Age'] < 18]['Survived'].mean()
print(round(child_s,2))
p_f1 = df[(df['Sex'] == 'female' ) & (df['Pclass'] == 1)]
p_female_first_class = len(p_f1) / len(df)
print(p_female_first_class)

'''''''''
# Step 1 — filter for your condition
#subset = df[df['column'] == value]

# Step 2 — measure what you want
#probability = subset['target'].mean()
# or
#probability = len(subset) / len(df)

#female_3=df[( df['Sex'] == 'female') & (df['Pclass'] == 3)]
#print(round(female_3['Survived'].mean(),2))

#print(len(female_3)/len(df))
#len(subset) / len(df) # what fraction of all passengers were x
#subset['Survived'].mean() of people who were x, how many survived



df = pd.read_csv('titanic.csv')
# did survivors and non - survivors pay differen fares
survived_fare = df[df['Survived'] ==1]['Fare']
died_fare = df[df['Survived'] ==0]['Fare']

#The t-test — comparing two groups
#The most common test. Checks if two groups have meaningfully different means:
'''''''''
t_stat, p_value = stats.ttest_ind(survived_fare, died_fare)
print(f"T-statistics: {round(t_stat,3)}")
print(f"P-Value {round(p_value,5)}")

if p_value < 0.05:
    print('Result:statistically significant')
else:
    print("Result not significant")


#The chi-square test — comparing categories
#Used when both variables are categorical (like gender and survival):

contingency = pd.crosstab(df['Sex'], df['Survived'])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
print(f"P-Value is: {round(p_value,10)}")

if p_value < 0.05:
    print('Gender and survival are significantly related')
else:
    print('No significant relationship') 

con=pd.crosstab(df['Fare'], df['Survived'])
chi2,p_value, dof, expected = stats.chi2_contingency(con)
print(round(p_value,2))
if p_value < 0.05:
    print('Statistically significant')
else:
    print('no relatnionship')
'''

df = pd.read_csv('titanic.csv')

#H0: survivors don't pay significantly different fares than non survivors
#H1: survivors pay significantly different fares than non survivors
survivors_fare = df[df['Survived'] ==1]['Fare']
non_survivors_fare = df[df['Survived'] ==0]['Fare']
t_stat, p_value = stats.ttest_ind(survivors_fare, non_survivors_fare)
print(round(t_stat,5))
print(round(p_value,2))

if p_value < 0.05:
    print('Statistically significant')
else:
    print('Statistically not significant')
#comment - survivors pay significantly different fares than non survivors p_value <0.05


# H0:There is no relationship between pclass and survived rate
# H1: There is relationship between pclass and survived rate
contingency = pd.crosstab(df['Pclass'], df['Survived'])

chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

print(round(p_value,2))

if p_value < 0.05:
    print('Significantly related')
else:
    print('Not significant related')

# comment- There is relationship between pclass and survived rate


age_survivors = df[df['Survived'] ==1]['Age'].dropna()
age_non_survived = df[df['Survived'] ==0]['Age'].dropna()

t_test, p_value = stats.ttest_ind(age_survivors,age_non_survived)

print(round(t_test,2))
print(round(p_value,2))

if p_value < 0.05:
    print('Statistically significant')
else:
    print('Statistically not significant')

