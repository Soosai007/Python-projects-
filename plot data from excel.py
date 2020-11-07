import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("time_series_covid_19_deaths.csv")
df.plot()
plt.show()
