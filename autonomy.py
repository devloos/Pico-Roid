import util
import time


def forward_square():
    util.forward()
    time.sleep(1)
    util.right()
    time.sleep(.55)
    util.forward()
    time.sleep(1)
    util.right()
    time.sleep(.55)
    util.forward()
    time.sleep(1)
    util.right()
    time.sleep(.55)


def reverse_square():
    util.backward()
    time.sleep(1)
    util.left()
    time.sleep(.55)
    util.backward()
    time.sleep(1)
    util.left()
    time.sleep(.55)
    util.backward()
    time.sleep(1)
    util.left()
    time.sleep(.55)
