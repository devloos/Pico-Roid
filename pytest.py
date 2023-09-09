import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(27, GPIO.HIGH)

pwm = GPIO.PWM(12, 100)
pwm.start(100)

try:
    speed = 100
    while True:
        if speed > 0:
            speed = speed - 5
            pwm.ChangeDutyCycle(speed)

        time.sleep(1)

except:
    pwm.stop()
    GPIO.cleanup()
