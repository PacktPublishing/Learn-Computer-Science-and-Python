import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

plt.xticks([])
plt.yticks([])

plt.plot(0,0,'wo', markersize=1)
plt.plot(300,300,'wo', markersize=1)

plt.plot(150,150,'yo', markersize=200) 
plt.plot(150,150,'ko', markersize=150) 
plt.plot(150,160,'yo', markersize=150)

plt.plot(120,190,'ko', markersize=40)
plt.plot(180,190,'ko', markersize=40)

plt.grid()
plt.show()