import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
   while True:

      input_state = GPIO.input(18)
      if(input_state == False):
	GPIO.output(2, GPIO.LOW)      	
      	time.sleep(0.2)
	GPIO.output(2, GPIO.HIGH)


# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
