import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(15, 45, 100).round(1)
noise = np.random.uniform(-1, 5, 100).round(1)
y = (x - 5) + noise

plt.xlabel('Cricket Chirp / 15 seconds')
plt.ylabel("Temperature / Celsius")
plt.title("Cricket Chirps vs Temperature")
plt.grid(True)
plt.plot(x,y, 'ro')

# ডাটাগুলো CSV ফাইলে সেভ করার জন্য
data_to_save = np.column_stack((x, y)) # x এবং y কে কলাম হিসেবে সাজানো
np.savetxt("f:\\aiml\\M2\\data-ploting\\chirps_data.csv", data_to_save, delimiter=",", header="Chirps,Temperature", comments="", fmt='%.1f')
print("Data saved to chirps_data.csv")

plt.show()