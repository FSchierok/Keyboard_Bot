from pynput import mouse, keyboard
from random import uniform
from time import sleep
Keyboard = keyboard.Controller()
Mouse = mouse.Controller()

with open("pos.txt", "r") as f:
    pos = f.readlines()
pos1 = pos[0].split("<>")
pos2 = pos[1].split("<>")
while True:
    Keyboard.press("w")
    Keyboard.press("a")
    sleep(uniform(1, 5))
    Keyboard.release("a")
    sleep(uniform(1, 3))
    Keyboard.press("d")
    sleep(uniform(1, 3))
    Keyboard.release("w")
    sleep(uniform(1, 3))
    Keyboard.release("d")
    sleep(uniform(1, 5))
    Keyboard.press(Keyboard.Key.enter)
    sleep(uniform(0.1, 0.3))
    Keyboard.release(Keyboard.Key.enter)
    Mouse.position(int(pos1[0]), int(pos1[1]))
    Mouse.click(mouse.Button.left)
    sleep(uniform(0.2, 0.4))
    Mouse.position(int(pos2[0]), int(pos2[1]))
    Mouse.click(mouse.Button.left)
    sleep(uniform(0.2, 0.4))
    Mouse.click(mouse.Button.right)
    sleep(uniform(0.1, 0.5))
