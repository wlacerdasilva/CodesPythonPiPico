# Data Logger temperature
# Por: Wilton Lacerda Silva
# 06/2021
# Este vídeo: https://youtu.be/B9kwmgtZf4Q

import machine, onewire, ds18x20, utime
 
pino = machine.Pin(0)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(pino))
 
id_sensor = ds_sensor.scan()[0] #Somente 1 sensor
print('Dispositivo encontrado:',id_sensor)
 
while True:
  ds_sensor.convert_temp()
  utime.sleep(0.750)
  print(ds_sensor.read_temp(id_sensor), "°C")
  utime.sleep(2)