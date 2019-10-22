from easytello import tello
import time
import serial

speed = 50

cur_x = 0
cur_y = 0
cur_z = 0

arduinoData = serial.Serial('com5',9600)

def led_on():
        arduinoData.write('1'.encode())
        print ("on")

def led_off():
        arduinoData.write('0'.encode())
        print ("off")

def flyto(x, y, z, speed):
        global cur_x
        global cur_y
        global cur_z

        print ("current: ", cur_x,cur_y,cur_z)

        dif_x = x - cur_x
        dif_y = y - cur_y
        dif_z = z - cur_z
        
        cur_x += dif_x
        cur_y += dif_y
        cur_z += dif_z
        
        drone.go(dif_x,dif_y,dif_z,speed)

with open('cube.txt') as file:
    coordinate_list = file.read().splitlines()

drone = tello.Tello()
print(drone.get_battery())

drone.takeoff()
drone.wait(1)

for i in range(len(coordinate_list)): 
        if (coordinate_list[i] == 'on'):
                led_on()
                drone.wait(1)
        elif (coordinate_list[i] == 'off'):
                led_off()
                drone.wait(1)
        else:
                x,y,z = coordinate_list[i].split(',')
                x = int(x)
                y = int(y)
                z = int(z)
                flyto (y, -x, z, speed)


drone.wait(1)	
drone.land()
print(drone.get_battery())


