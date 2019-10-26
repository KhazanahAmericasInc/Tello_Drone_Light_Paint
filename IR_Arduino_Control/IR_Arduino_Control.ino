
//Craig Crundwell
//Oct 20 019

//This program recieves commands from a python program to control the tello lights
//The python program controls the drone over wifi and coordinates the timing of the lights on the drone
//The python program sends commands over serial to tell the arduino when to change the lights
//This program is run on the ardunio Nano connected to IR lights to communicate with the IR reciever on the tello drone

#include <IRremote.h> //This library is used to send hex codes over IR

IRsend irsend; //Create a object called irsend of class IRsend

char serialData; //This stores the data sent from the python program

void setup() {
  pinMode(3, OUTPUT); //Pin 3 used for IR lights
  Serial.begin(9600);
}


void loop() {

  if(Serial.available() > 0)  { //Checks for serial data

    serialData = Serial.read(); //Reads serial data
    if(serialData == '1')
    {
      for (int i =0; i<20; i++)
      {
        irsend.sendNEC(0xF7C03F, 32); //Send on command
        delay(50);
      }
      
    }
    else if(serialData == '0')
    {
      for (int i =0; i<20; i++)
      {
        irsend.sendNEC(0xF740BF, 32); //Send off command
        delay(50);
      }
      
    }
  }  

}
