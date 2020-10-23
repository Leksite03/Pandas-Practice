import pandas as pd
import numpy as np

df=pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

#finding unique values
#find the unique value in col 2
print(df['col2'].unique())
#to find the number of unique value in col 2
print(df['col2'].nunique())

#to find a table and how many times it shows up
print(df['col2'].value_counts())


#selecting data
print(df[df['col1']>2])

#to combine conditions
print(df[(df['col1']>2)&(df['col2']==444)])

#apply method_to include your own functions

def times2(x):
	return x*2
	
print(df['col1'].apply(times2))

#it is also used to return the length of a col
print(df['col3'].apply(len))
#it can also work with lambda
print(df['col2'].apply(lambda x:x*2))

#removing cols
print(df.drop('col1',axis=1))
#to get the index of cols
print(df.columns)
#for index
print(df.index)
#sorting & ordering a dataframe
#if we want to arrange values
print(df.sort_values('col2'))

#to find null values_if there is a non null value it returns false
print(df.isnull())

#pivot tables

data={'A':['foo','foo','foo','bar','bar','bar'],'B':['one','one','two','two','one','one'],'C':['x','y','x','y','x','y'],'D':[1,3,2,5,4,1]}
df=pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D',index=['A','B'],columns=['C']))