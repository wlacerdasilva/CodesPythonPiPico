# Data Logger temperature
# Por: Wilton Lacerda Silva
# 06/2021
# Este vídeo: https://youtu.be/B9kwmgtZf4Q

import machine, onewire, ds18x20, utime

pino = machine.Pin(0)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(pino))
 
id_sensor = ds_sensor.scan()[0] #Somente 1 sensor
print('Dispositivo encontrado:',id_sensor)

nom_Arq = "Dat_temp_01.txt"
file = open(nom_Arq, "w")
print("Iniciando a gravação do Arquivo: " + nom_Arq)
t1 = 0.750 #Tempo mínimo obrigatório para conversão completa
t2 = 0.750
t = t1 + t2

for n in range(10):
    ds_sensor.convert_temp()
    utime.sleep(t1)
    temp_sens = ds_sensor.read_temp(id_sensor)
    print(str(n*t)+"s " + str(temp_sens) + "°C")
# Write a text to file
    file.write(str(n*t) + "s " + str(temp_sens) + "°C\n")
# The file remains open for write
    file.flush()
    utime.sleep(t2)

file.close()
print("Arquivo: " + nom_Arq + " finalizado.")