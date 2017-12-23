from pykeyboard import PyKeyboard
import time

k=PyKeyboard()
time.sleep(5)

for i in range(0,10):
    k.tap_key(k.right_key)
    time.sleep(3)