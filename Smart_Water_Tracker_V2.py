import matplotlib.pyplot as plt
import numpy as np
import csv

NYC_water_file = open("NYC_Water.csv", "a")

NYC_water_file.write("\n2019,8239493,910,105")
NYC_water_file.write("\n2020,8230000,900,99")

NYC_water_file.close()

data = np.loadtxt("NYC_Water.csv", unpack = True, delimiter = ",")

#x = np.linspace(1979, 2018, 10)
#y = np.linspace(7, 9, 10)
#y2 = np.linspace(900, 1520, 10)
#y3 = np.linspace(100, 250, 10)


ax = plt.subplot()

#plt.figure()
#plt.plot(x, y, "")
plt.subplot(311)
plt.plot(data[0], data[1], "r")
ax.set_xlabel(" Time (Years)")
plt.title("NYC Urban Water Usage Attributes (1979 to 2018)")
plt.ylabel("NYC Population")
#plt.axis(1979, 2018, 7000000, 8500000)

#plt.plot(x, y2, "")
plt.subplot(312)
plt.plot(data[0], data[2], "g")
ax.set_xlabel("Time (Years)")
plt.ylabel("NYC Consumption (MGD)")
#plt.axis(1979, 2018, 900, 1512)

#plt.plot(x, y3, "")
plt.subplot(313)
plt.plot(data[0], data[3], "b")
ax.set_xlabel("Time (Years)")
plt.ylabel("Per Capita (GPD)")
#plt.axis(1979, 2018, 100, 213)  

plt.show()
