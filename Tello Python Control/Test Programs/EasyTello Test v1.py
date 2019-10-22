from easytello import tello
import time

my_drone = tello.Tello()

print(my_drone.get_battery())

my_drone.takeoff()

my_drone.wait(1)

for i in range(4):
	my_drone.forward(100)
	my_drone.cw(90)

my_drone.wait(1)	
my_drone.land()

print(my_drone.get_battery())

#go(self, x: int, y: int, z: int, speed: int):
