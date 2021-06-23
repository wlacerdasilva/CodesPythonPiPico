# Data Logger
# Por: Wilton Lacerda Silva
# 06/2021
# Este vídeo: https://youtu.be/Erkl7Rmc85A

import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('Data01.txt')

x = data[:,0]
y = data[:,1]
plt.plot(x,y,'ro')
plt.title("Gráfico do potenciometro")
plt.xlabel("tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid()
plt.show()