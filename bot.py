from pynput.keyboard import Key, Controller
from random import randint
from time import sleep
keyboard = Controller()
while True:
    keyboard.press("w")
    keyboard.press("a")
    sleep(randint(1, 5))
    keyboard.release("a")
    sleep(randint(1, 3))
    keyboard.press("d")
    sleep(randint(1, 3))
    keyboard.release("w")
    sleep(randint(1, 3))
    keyboard.release("d")
    sleep(randint(1, 5))
    keyboard.press(Key.enter)
    sleep(0.1 * randint(2, 4))
    keyboard.release(Key.enter)
    sleep(randint(2, 4))
    keyboard.press(Key.enter)
    sleep(0.1 * randint(2, 4))
    keyboard.release(Key.enter)
    sleep(randint(1, 4))
