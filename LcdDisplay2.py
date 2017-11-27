#!/usr/bin/python
#Chris Searl
#LCD Display
#http://heinrichhartmann.com/blog/2014/12/14/Sensor-Monitoring-with-RaspberryPi-and-Circonus.html
# Datasheet: http://www.ti.com/lit/ds/symlink/adc0838-n.pdf
# Part of SunFounder LCD StarterKit
# http://www.sunfounder.com/index.php?c=show&id=21&model=LCD%20Starter%20Kit
# Modified this to add return floating number, and voltage per bit.
# Steps to wire came from Logan
#-------------------------------------------------------------------------------
# __To wire__
# Pin 1 of ADC to #17 on T-cobler
# Pin 2 of ADC to middle of potometer on T-cobler
# Pin 3 of ADC to ground on board
# Pin 4 of ADC to ground on board
# Pin 5 of ADC to #22 on T-cobler
# Pin 6 of ADC to #27 on T-cobler
# Pin 7 of ADC to #18 on T-cobler
# Pin 8 of ADC to to 3.3V on T-cobler
# Then you hook up the two outsides wires of the potometer
# One to 3.3V on the cobblerand the other to ground on the board
#Using a 5k potentiometer
#Analog input ADC0832 chip
#--------------------------------------------------------------------------------
import subprocess
import time
import os
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()

GPIO.setmode(GPIO.BCM)
#bits for 3.3 volts input
VOLTAGEPERBIT=(3.3/255)

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
PIN_CLK = 18
PIN_DO  = 27
PIN_DI  = 22
PIN_CS  = 17

# set up the SPI interface pins
GPIO.setup(PIN_DI,  GPIO.OUT)
GPIO.setup(PIN_DO,  GPIO.IN)
GPIO.setup(PIN_CLK, GPIO.OUT)
GPIO.setup(PIN_CS,  GPIO.OUT)

# read SPI data from ADC8032
def getADC(channel):
	# 1. CS LOW.
        GPIO.output(PIN_CS, True)      # clear last transmission
        GPIO.output(PIN_CS, False)     # bring CS low

	# 2. Start clock
        GPIO.output(PIN_CLK, False)  # start clock low

	# 3. Input MUX address
        for i in [1,1,channel]: # start bit + mux assignment
                 if (i == 1):
                         GPIO.output(PIN_DI, True)
                 else:
                         GPIO.output(PIN_DI, False)

                 GPIO.output(PIN_CLK, True)
                 GPIO.output(PIN_CLK, False)

        # 4. read 8 ADC bits
        ad = 0
        for i in range(8):
                GPIO.output(PIN_CLK, True)
                GPIO.output(PIN_CLK, False)
                ad <<= 1 # shift bit
                if (GPIO.input(PIN_DO)):
                        ad |= 0x1 # set first bit

        # 5. reset
        GPIO.output(PIN_CS, True)

        return ad * VOLTAGEPERBIT

if __name__ == "__main__":
        while True:
                print "ADC[0]: {}\t ADC[1]: {}".format(getADC(0), getADC(1))
                
                Output_String = "Voltage is: %.3f \t ADC[1]: %.3f" %(getADC(0), getADC(1))

                time.sleep(1.5)
                lcd.message(Output_String)
                time.sleep(1.5)
                lcd.clear()
                continue
