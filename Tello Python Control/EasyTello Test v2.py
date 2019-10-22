from easytello import tello
import time

drone = tello.Tello()

print(drone.get_battery())

drone.takeoff()

drone.wait(1)

drone.go(0,0,100,50)


drone.go(100,100,0,50)
drone.go(100,0,0,50)    
drone.go(100,-100,0,50)
drone.go(0,-100,0,50)
drone.go(100,-100,0,50)
drone.go(-100,0,0,50)
drone.go(-100,100,0,50)
drone.go(0,100,0,50)

drone.wait(1)	
drone.land()

print(drone.get_battery())

#go(self, x: int, y: int, z: int, speed: int):
#drone.cw(90)
#drone.ccw(90)
