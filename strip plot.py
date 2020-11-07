# import the seaborn libaray 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
df = sns.load_dataset('tips') 
sns.set(style="whitegrid")
sns.stripplot(x ='day', y ='total_bill', data = df,jitter = True, hue ='smoker', dodge = True)
plt.show()



