import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
df = sns.load_dataset('tips') 
sns.set(style="whitegrid")

sns.boxplot(x ='day', y ='total_bill', data = df, hue ='smoker') 
plt.show()
