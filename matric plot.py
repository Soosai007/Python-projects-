# import the necessary libraries 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt  

# load the flights dataset 
fd = sns.load_dataset('flights') 

# make a dataframe of the data 
df = pd.pivot_table(values ='passengers', index ='month', columns ='year', data = fd) 

# make a clustermap from the dataset 
sns.heatmap(df, cmap ='plasma', annot=True,linewidths=1,linecolor='white')
plt.show()
