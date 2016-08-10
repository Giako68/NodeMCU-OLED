#
# Scrolling Demo using SSD1306 128x64 OLED display
#

from SSD1306 import SSD1306
from ustruct import unpack

def Demo(speed=2):
    Display = SSD1306(scl=4, sda=5, addr=60)
    F = open("DemoBack.dat", "rb")
    I = F.read()
    F.close()
    Display.SetWriteWindow(0, 7, 0, 127)
    Display.SendData(I)
    F = open("DemoScrolling.dat", "rb")
    I = F.read(2)
    W = unpack("<H", I)[0]
    I = F.read(W * 4)
    F.close()
    x = 0
    while(True):
         Display.SetWriteWindow(2, 5, 0, 127)
         if (x < (W - 128)):
            Display.SendData(I[x*4:(x+128)*4])
         else:
            Display.SendData(I[x*4:W*4])
            Display.SendData(I[0:(x-W+128)*4])
         x = (x + speed) % W
            
