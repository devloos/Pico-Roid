import RPi.GPIO as IO


def stop():
    IO.output(23, IO.HIGH)
    IO.output(24, IO.HIGH)

    IO.output(22, IO.HIGH)
    IO.output(27, IO.HIGH)


def forward():
    IO.output(23, IO.HIGH)
    IO.output(24, IO.LOW)

    IO.output(22, IO.LOW)
    IO.output(27, IO.HIGH)


def backward():
    IO.output(23, IO.LOW)
    IO.output(24, IO.HIGH)

    IO.output(22, IO.HIGH)
    IO.output(27, IO.LOW)


def left():
    IO.output(23, IO.HIGH)
    IO.output(24, IO.HIGH)

    IO.output(22, IO.HIGH)
    IO.output(27, IO.LOW)


def right():
    IO.output(23, IO.HIGH)
    IO.output(24, IO.LOW)

    IO.output(22, IO.HIGH)
    IO.output(27, IO.HIGH)
