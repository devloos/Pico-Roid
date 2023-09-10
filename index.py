import RPi.GPIO as IO

IO.setmode(IO.BCM)

IO.setup(23, IO.OUT)
IO.setup(24, IO.OUT)

IO.setup(22, IO.OUT)
IO.setup(27, IO.OUT)


try:
    while True:
        pass
except:
    IO.cleanup()
