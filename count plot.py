# import the seaborn libaray 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
df = sns.load_dataset('tips') 
sns.set(style="whitegrid")
sns.countplot(x ='sex', data = df) 

plt.show()
