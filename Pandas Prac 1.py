import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#to select a col from the data frame.
print(df['W'])

#to select more than one col
print(df[['W','Y']])

#creating a new col
df['new']=df['W']+df['Y']
print(df)

#to remove a new col using drop()
print(df.drop('new',axis=1,inplace=True))
#note:if inplace =True is added it becomes permanent

#to remove a row using drop()
print(df.drop('A'))

print(df.shape)

#selectimg rows
print(df.loc['A'])

#using iloc[]
print(df.iloc[2])

#selecting a subset of row and col
print(df.loc['B','Y'])

#also
print(df.loc[['A','B'],['W','Y']])




#conditional selection
print(df>0)

print(df[df>0])
'''when using conditional statement for the whols dataframe,the false ones will change to nan but if you are specifying from a row or col it does not print out the false ones'''

#grabbing all the rows where z is less than zero
print(df[df['Z']<0])
#where w is grater than 0
print(df[df['W']>0])
#return the col X & Ywhere w is greater than 0
print(df[df['W']>0][['X','Y']])
#or
boolx=df['W']>0
result=df[boolx]
print(result[['Y','X']])

#multiple condition
#or(|)
print(df[(df['W']>0) | (df['Y']>1)])
#and(&)
print(df[(df['W']>0)&(df['Y']<1)])

#resetting the index to default
print(df.reset_index)

#another method for changing the index
newind='CA NY WY OR CO'.split()
df['States']=newind
print(df)
print(df.set_index('States'))