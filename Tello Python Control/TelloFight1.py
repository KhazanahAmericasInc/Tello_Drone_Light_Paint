import tello1
import time

t = tello1.Tello('192.168.10.2', 8888)

distance = int(1)

t.set_speed(1)

print(t.get_battery())
time.sleep(2)
t.takeoff()
time.sleep(2)
t.move('back', distance)
time.sleep(5)
t.flip('b')
time.sleep(2)
t.land()
time.sleep(2)
print(t.get_battery())




