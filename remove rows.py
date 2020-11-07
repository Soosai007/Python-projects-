# importing pandas module 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv") 


# replacing na values in college with No college 
data["College"].fillna("No College", inplace = True) 

df=data 


# saving the dataframe 
df.to_csv('output.csv') 
