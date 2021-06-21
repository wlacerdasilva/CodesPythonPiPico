# Data Logger
# Por: Wilton Lacerda Silva
# 06/2021
# Video relacionado:   https://www.youtube.com/watch?v=wf9nKxsWiOo
# Este vídeo: https://youtu.be/_8fyoArNteY

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime

# Escolha dos pinos do I2C
i2c = I2C(0,sda=Pin(16),scl=Pin(17),freq=100000)
# Criar e instanciar um objeto oled
oled = SSD1306_I2C(128,64,i2c)
# Criar e intanciar objetos led e botão
led_onboard = machine.Pin(25, Pin.OUT)
# O pino do botão foi setado com um resistor de pull_down
button = machine.Pin(15,Pin.IN, Pin.PULL_DOWN)
# Configuração dos ADCs
adc_0 = ADC(28) #GP28 equivale ao canal 2
sensor_temp = ADC(4) #Canal 4 Temperatura
conversion_factor = 3.3 / (65535)

# Open a file for writting.
f_name = "Data_pot_temp_"
f_ext  = ".txt"
cont = 0
nom_Arq = f_name + str(cont) + f_ext
file = open(nom_Arq, "w")

#Inicialização do Display
oled.fill(0) #Preenchimento com 0 ou 1
oled.text("Gab. Tecnologia",2,4) #Texto e posição(x,y)
oled.rect(0,0,128,15,1)
oled.rect(0,16,16,16,1)
oled.text("0",20,20)
oled.show() #Apresenta no display

sinalizador  = True
n_samples = 0;
print("Pressione o Push Button para capturar dados...")

while True:

    if button.value() == True and sinalizador == True:
        led_onboard.value(1)
        oled.fill_rect(0,16,16,16,1)
        cont = cont + 1
        oled.fill_rect(20,16,24,16,0)
        oled.text(str(cont),20,20)
        oled.show()
        sinalizador = False
        utime.sleep(0.2)
    if button.value() == True and sinalizador == False:
        led_onboard.value(0)
        oled.fill_rect(0,16,16,16,0)
        oled.rect(0,16,16,16,1)
        oled.show()
        sinalizador = True
        file.close()
        print("Arquivo: " + nom_Arq + " finalizado.")
        print("Pressione o Push Button para capturar dados...")
        nom_Arq = f_name + str(cont) + f_ext
        file = open(nom_Arq, "w")
        n_samples = 0
        utime.sleep(0.2)
    valor = adc_0.read_u16()*conversion_factor
    oled.fill_rect(50,16,30,16,0)
    oled.text(str(round(valor,1)),50,20)
    temperatura = sensor_temp.read_u16()*conversion_factor
    temperatura = 27 - (temperatura - 0.706)/0.001721
    oled.fill_rect(80,16,48,16,0)
    oled.text(str(round(temperatura,1)),90,20)
    oled.show()
    
    if sinalizador == False:
        print(str(n_samples)+ " | " + str(valor) + "V | " + str(temperatura) +"C\n")
        # Write a text to file
        file.write(str(n_samples)+ " | " + str(valor) + "V | " + str(temperatura) +"C\n")
        # The file remains open for write
        file.flush()
        n_samples = n_samples + 1

    #utime.sleep(0.3)

