# Data Logger
# Por: Wilton Lacerda Silva
# 06/2021
# Este vídeo: https://youtu.be/Erkl7Rmc85A

from machine import Pin, ADC
import utime
conversion_factor = 3.3 / (65535)
pot = machine.ADC(28)
contador = 1;
nom_Arq = "Data01.txt"
file = open(nom_Arq, "w")
for n in range(100):
    valor = pot.read_u16()*conversion_factor
    print(str(contador) + " | Valor =",str(valor),"V")
    file.write(str(contador)+ " " + str(valor) +"\n")
    file.flush()
    contador = contador + 1
    utime.sleep(0.1)
else:
    file.close()
    print("Arquivo: " + nom_Arq + " finalizado.")
