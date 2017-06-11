import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 14, 15]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# main loop

try:
   while True:

      for i in pinList:
         GPIO.output(i, GPIO.LOW)         
	 time.sleep(0.1)
         GPIO.output(i, GPIO.HIGH) 




# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


