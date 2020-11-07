# import the seaborn libaray 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
df = sns.load_dataset('tips') 
sns.set(style="whitegrid")
sns.swarmplot(x ='day', y ='total_bill', data = df) 
plt.show()
