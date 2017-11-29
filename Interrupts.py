#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3  
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
import time
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.  
# Both ports are wired to connect to GND on button press.  
# So we'll be setting up falling edge detection for both  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
# GPIO 24 set up as an input, pulled down, connected to 3V3 on button press  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
# now we'll define two threaded callback functions  
# these will run in another thread when our events are detected  
def my_callback(channel):  
    lcd.clear()
    lcd.message("Falling edge\non port 24!")
    print ("Rising edge detected on port 24 - even though, in the main thread,")
    print ("we are still waiting for a falling edge in the main thread")
    raw_input(lcd.message("Press Enter n>"))

  
 # The GPIO.add_event_detect() line below set things up so that
# when a rising edge is detected on port 24, regardless of whatever
# else is happening in the program, the function "my_callback" will be run
# It will happen even while the program is waiting for
# a falling edge on the other button.

GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime = 200)
          
try:
    lcd.clear()
    lcd.message("Waiting \n Port 23")
    print "Waiting for falling edge on port 23"
    GPIO.wait_for_edge(23, GPIO.FALLING)
    lcd.clear()
    lcd.message("Excellent work")
    print "Falling edge detected."

    
except KeyboardInterrupt:
    GPIO.cleanup() # clean up GPIO on CTRL+C exit
GPIO.cleanup() # clean up GPIO on normal exit

