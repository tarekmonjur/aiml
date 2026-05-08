import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.random.uniform(15, 45, 100).round(1)
noise = np.random.uniform(-1, 3, 100).round(1)
y = (x - 5) + noise

# সরাসরি NumPy অ্যারে থেকে DataFrame তৈরি (CSV ফাইল রাইট/রিড করার প্রয়োজন নেই)
df = pd.DataFrame({'Chirps': x, 'Temperature': y})

g = sns.lmplot(x="Chirps", y="Temperature", data=df)

# টাইটেল এবং লেবেল যোগ করার প্রফেশনাল উপায়
g.set_axis_labels("Cricket Chirps / 15s", "Temperature / Celsius")
plt.title("Relationship: Chirps vs Temperature", pad=20)
plt.show()