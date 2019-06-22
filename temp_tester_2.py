import matplotlib.pyplot as plt
import numpy as np
import csv

x = np.linspace(1979, 2018, 25)
#y = np.linspace(800, 2000, 25)

data = np.loadtxt("NYC_Water.csv", unpack = True, delimiter = ",")

plt.plot(x, x, label = "Water Consumption (MGD)")
#plt.plot(x, x**2, label = "NYC Population")
#plt.plot(x, x**3, label = "Per Capita (GPD)")

plt.plot(data[0], data[2])
#plt.plot(data[0], data[1])
#plt.plot(data[0], data[3])
plt.axis([1979, 2018, 900, 1512])

plt.xlabel('Time (Years)')
plt.ylabel('NYC Consumption')

plt.title("NYC Water Demand")

#plt.legend()
plt.show()
