# Tello_Drone_Light_Paint


#### **Summary**
-The tello drone is controlled through a python program over wifi
-The python program communicates over serial to an arduino uno that uses IR to control the drone lights
-A file with coordinates is read by the python program to control the drone along a specific path

#### **Tello Drone Control**
-The EasyTello library is used for control of the drone

#### **Light Control**
-an IR led strip receiver is used to control the lights
-a 5v regulator is connected to a 1 cell lipo to supply 5v to the controller
-An arduino connected to a proto-board with 20 IR Led's and a transistor is used to send IR commands to the receiver
-The whole setup is put inside of a 3d printed case with translucent material

