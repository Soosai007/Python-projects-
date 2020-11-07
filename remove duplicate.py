# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("employees.csv") 


# dropping ALL duplicte values 
data.drop_duplicates(subset ="First Name",keep = 'first', inplace = True)

df=data

# saving the dataframe 
df.to_csv('output.csv')


