import RPi.GPIO as GPIO
import util

GPIO.setmode(GPIO.BCM)


GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


try:
    stop()
    while True:
        reverse_square()

except:
    stop()
    GPIO.cleanup()
