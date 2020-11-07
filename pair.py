#pair plot 

import matplotlib.pyplot as plt 
import seaborn as sns;
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris)
plt.show()
