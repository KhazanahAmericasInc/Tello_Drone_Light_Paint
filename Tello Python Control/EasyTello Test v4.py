from easytello import tello
import time

cur_x = 0
cur_y = 0
cur_z = 0
on = 0

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

with open('output.txt') as file:
    coordinate_list = file.read().splitlines()

drone = tello.Tello()
print(drone.get_battery())

drone.takeoff()
drone.wait(1)

for i in range(len(coordinate_list)): 
        if (coordinate_list[i] == 'on'):
                drone.cw(180)
                on = 1
                print ("on")
        elif (coordinate_list[i] == 'off'):
                drone.ccw(180)
                on = 0
                print ("off")
        else:
                x,y,z = coordinate_list[i].split(',')
                x = int(x)
                y = int(y)
                z = int(z)
                if (on ==1):
                        flyto (-y, x, z, 50)
                else:
                        flyto (y, -x, z, 50)

drone.wait(1)	
drone.land()
print(drone.get_battery())


