import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

chirp_data = pd.read_csv("chirps_data.csv")
g = sns.lmplot(x="Chirps", y="Temperature", data=chirp_data)
plt.title("Cricket Chirps vs Temperature")
plt.show()