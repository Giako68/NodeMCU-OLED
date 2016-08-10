#
# Simple SSD1306 driver for ESP8266 & MicroPython
#

from machine import Pin, I2C
from ustruct import pack

class SSD1306(object):
      def __init__(self, scl, sda, addr):
          self.Bus = I2C(scl=Pin(scl), sda=Pin(sda), freq=400000)
          self.Addr = addr
          self.SendCommand(pack("26B",  0xAE,0xD5,0x80,0xA8,0x3F,0xD3,0x00,0x40,0x8D,0x14,0x20,0x01,0xA1,0xC8,0xDA,0x12,0x81,0xCF,0xD9,0xF1,0xDB,0x40,0x2E,0xA4,0xA6,0xAF))
          
      def SendCommand(self, Cmd):
          Msg = pack("BB", self.Addr<<1, 0x00) + Cmd
          self.Bus.start()
          self.Bus.write(Msg)
          self.Bus.stop()

      def SendData(self, Data):
          Msg = pack("BB", self.Addr<<1, 0x40) + Data
          self.Bus.start()
          self.Bus.write(Msg)
          self.Bus.stop()

      def SetWriteWindow(self, PageStart, PageStop, ColStart, ColStop):
          if (PageStart < 0) or (PageStop > 7) or (PageStart > PageStop):
             return(-1)
          if (ColStart < 0) or (ColStop > 127) or (ColStart > ColStop):
             return(-1)
          self.SendCommand(pack("6B", 0x21, ColStart, ColStop, 0x22, PageStart, PageStop))
          return(0)
