import pandas as pd
import numpy as np
from numpy.random import randn

#multindex and index hier key
#index levels

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)

print(hier_index)
print(list(zip(outside,inside)))

df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

#selecting from the very outside
print(df.loc['G1'])
#to select row 1 under G1
print(df.loc['G1'].loc[1])

#to give names to the index
df.index.names=['Groups','Num']
print(df)

#to select from the inside
print(df.loc['G1'].loc[2]['B'])
#another
print(df.loc['G2'].loc[3]['A'])

#using xs()
print(df.xs('G1'))

#selecting values under the inner index 1 under both G1 and G2
print(df.xs(1,level='Num'))