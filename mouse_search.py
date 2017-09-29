from pynput.mouse import Controller
from time import sleep
Mouse = Controller()
sleep(10)
x1, y1 = Mouse.position()
sleep(3)
x2, y2 = Mouse.position()
with open("pos.txt", "w") as f:
    f.write(str(x1) + "   " + str(y1) + "\n")
    f.write(str(x2) + "   " + str(y2))
