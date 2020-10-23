import pandas as pd
import numpy as np

d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df=pd.DataFrame(d)
print(df)

#dropna()
#to drop any row with nan value
print(df.dropna())
#to drop any col with nan value
print(df.dropna(axis=1))
#to specify a thresh arg i.e to specify the minimum number of non nan value in other not to drop everything
print(df.dropna(thresh=2))

#fillna()
#to fill the nan values present
print(df.fillna(value='Fill value'))

#to fill the nan values with the mean of the col
print(df['A'].fillna(value=df['A'].mean()))