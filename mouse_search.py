from pynput.mouse import Controller
from time import sleep
import winsound
Freq = 2500
Dur = 500
Mouse = Controller()
sleep(10)
x1, y1 = Mouse.position
winsound.Beep(Freq, Dur)
sleep(3)
x2, y2 = Mouse.position
winsound.Beep(Freq, Dur)
with open("pos.txt", "w") as f:
    f.write(str(x1) + "   " + str(y1) + "\n")
    f.write(str(x2) + "   " + str(y2))
