#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial       # This is required for serial communication.

HIGH = "HIGH"
LOW = "LOW"
INPUT = "INPUT"
OUTPUT = "OUTPUT"

class Arduino(object):

    __OUTPUT_PINS = []      # For storing all the output pins. Used in closeAll() function.

    def __init__(self, port, baudrate=9600):
        self.serial = serial.Serial(port, baudrate)
        self.serial.write(b'99')

    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)

    def pinMode(self, pin, setTo):
        self.__sendData('0')
        self.__sendData(pin)
        if setTo=='OUTPUT' or '1':
            self.__sendData('1')
            print ("pin", pin,"set to OUTPUT")
            self.__OUTPUT_PINS.append(pin)
        elif setTo=='INPUT' or '0':
            self.__sendData('0')
            print ("pin", pin,"set to INPUT")
        return True

    def  digitalWrite(self, pin,setTo):
        self.__sendData('1')
        self.__sendData(pin)
        if setTo=='HIGH' or '1':
            self.__sendData('1')
            #print "Written HIGH on pin", pin
        elif setTo=='LOW' or '0':
            self.__sendData('0')
            #print "Written LOW on pin", pin
        return True

    def digitalRead(self, pin):
        self.__sendData('2')
        self.__sendData(pin)
        val=self.__getData()[0]
        if val==0:
            return "LOW"
        else:
            return "HIGH"

    def analogWrite(self, pin, setTo):
        self.__sendData('3')
        self.__sendData(pin)
        self.__sendData(setTo)
        #print "Written value", setTo, "on pin",pin
        return True

    def analogRead(self, pin):
        self.__sendData('4')
        self.__sendData(pin)
        return self.__getData()

    def closeAll(self):
        for each_pin in self.__OUTPUT_PINS:
            self.digitalWrite(each_pin, "LOW")
        return True

    def __sendData(self, serial_data):
        while(self.__getData()[0] != "w"):
            pass
        serial_data = str(serial_data).encode('utf-8')
        self.serial.write(serial_data)

    def __getData(self):
        input_string = self.serial.readline().decode('utf-8').rstrip('\n')
        return input_string

    def close(self):
        self.serial.close()
        return True
