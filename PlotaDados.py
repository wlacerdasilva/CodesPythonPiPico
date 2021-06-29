# Data Logger temperature
# Por: Wilton Lacerda Silva
# 06/2021
# Este vídeo: https://youtu.be/B9kwmgtZf4Q

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Data_temp_0.txt')

tempo = data[:,0]
temp_DS = data[:,1]
temp_PI = data[:,2]

plt.figure()
plt.plot(tempo,temp_DS,label="DS18B20")
plt.title("Temperatura")
plt.xlabel("tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend(loc = 'upper left')
plt.show()