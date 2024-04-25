import numpy as np 
import pandas as pd 

df:pd.DataFrame

# column_names = df.columns.to_list()
num_missing = df.isnull().sum()
shape = df.shape
num_rows = df.shape[0]
# num_cells = np.product(df.shape)

data = {
    # 'column_names': column_names, 
    'num_missing': num_missing, 
    'percent_missing (%)': [round(x,2) for x in num_missing/num_rows*100]
}

stats = pd.DataFrame(data)

stats[stats['num_missing'] != 0]

#replace missing values with the mean
numeric_data = df.select_dtypes(include=[np.number])
mean_value = numeric_data.mean()
numeric_data.fillna(value=mean_value, inplace=True)