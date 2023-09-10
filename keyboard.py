import tty
import sys
import termios
import util
import setup

setup.init()

orig_settings = termios.tcgetattr(sys.stdin)

tty.setcbreak(sys.stdin)
x = 0

try:
    while x != chr(27):  # ESC
        x = sys.stdin.read(1)[0]

        if x == 'w':
            util.forward()
        elif x == 's':
            util.backward()
        elif x == 'a':
            util.left()
        elif x == 'd':
            util.right()
except:
    setup.cleanup()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
