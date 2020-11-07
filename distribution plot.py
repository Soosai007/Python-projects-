# import thr necessary libraries 
import seaborn as sns 
import matplotlib.pyplot as plt 


# load the dataset 
df = sns.load_dataset('tips') 


# set the background style of the plot 
sns.set_style('whitegrid') 
sns.distplot(df['total_bill'], kde = True, color ='red') 
plt.show()
