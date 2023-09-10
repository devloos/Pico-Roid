import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)

IO.setup(12, IO.OUT)
IO.setup(27, IO.OUT)

IO.output(27, IO.HIGH)

pwm = IO.PWM(12, 100)
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
    IO.cleanup()
