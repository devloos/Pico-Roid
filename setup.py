import RPi.GPIO as IO
import util


def init():
    IO.setmode(IO.BCM)

    IO.setup(23, IO.OUT)
    IO.setup(24, IO.OUT)

    IO.setup(22, IO.OUT)
    IO.setup(27, IO.OUT)
    util.reset()


def cleanup():
    util.reset()
    IO.cleanup()
