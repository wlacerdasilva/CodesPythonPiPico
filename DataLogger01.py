# Data Logger
# Por: Wilton Lacerda Silva
# 06/2021
# Video relacionado:   https://www.youtube.com/watch?v=wf9nKxsWiOo
# Este vídeo: https://youtu.be/_8fyoArNteY

from machine import Pin, ADC
import utime


conversion_factor = 3.3 / (65535)
pot = machine.ADC(28)
contador = 1;
nom_Arq = "Dados02.txt"
# Open a file for writting.
file = open(nom_Arq, "w")
for n in range(10):
    valor = pot.read_u16()*conversion_factor
    print(str(contador) + " | Valor =",str(valor),"V")
    # Write a text to file
    file.write(str(contador)+ " | " + str(valor) +"\n")
    # The file remains open for write
    file.flush()
    contador = contador + 1
    utime.sleep(1)
else:
    file.close()
    print("Arquivo: " + nom_Arq + " finalizado.")
    
    
# file=open("Dados02.txt")
# print(file.read())
