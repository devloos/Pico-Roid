import RPi.GPIO as GPIO


def stop():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)

    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)


def forward():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)


def backward():
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)

    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)


def left():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)

    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)


def right():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

    GPIO.output(22, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
