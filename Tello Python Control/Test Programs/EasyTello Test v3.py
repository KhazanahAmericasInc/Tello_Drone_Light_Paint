from easytello import tello
import time

cur_x = 0
cur_y = 0
cur_z = 0

def flyto(x, y, z, speed):
        global cur_x
        global cur_y
        global cur_z

        dif_x = x - cur_x
        dif_y = y - cur_y
        dif_z = z - cur_z
        cur_x += dif_x
        cur_y += dif_y
        cur_z += dif_z

        drone.go(x,y,z,speed)

drone = tello.Tello()


print(drone.get_battery())

drone.takeoff()
drone.wait(1)

flyto (100,0,0,50)
flyto (100,100,0,50)
flyto (0,0,0,50)

drone.wait(1)	
drone.land()

print(drone.get_battery())

#go(self, x: int, y: int, z: int, speed: int):
#drone.cw(90)
#drone.ccw(90)


#Write own function to give absolute coordinate commands




