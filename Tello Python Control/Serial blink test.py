import time
import serial

arduinoData = serial.Serial('com5',9600)

def led_on():
        arduinoData.write('1'.encode())

def led_off():
        arduinoData.write('0'.encode())

while (1):
    print ("on")
    led_on()
    time.sleep(1)
    print ("off")
    led_off()
    time.sleep(1)
    
    
