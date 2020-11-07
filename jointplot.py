import seaborn as sns 
import matplotlib.pyplot as plt  
  
# to ignore the warnings  
from warnings import filterwarnings 
  
# load the dataset 
df = sns.load_dataset('tips') 

sns.jointplot(x ='total_bill', y ='tip', data = df) 

plt.show()
