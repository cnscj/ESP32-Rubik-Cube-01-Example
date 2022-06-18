import machine, neopixel
class LED():
   
    def __init__(self):
        self._color = False
        self._np = neopixel.NeoPixel(machine.Pin(5), 8) #5,8没怎么弄清楚
        
    def set_color(self,r,g,b):
        self._color = (r, g, b)
        self._np[0] = self._color
        self._np.write()
        
    def get_color(self):
        return self._color
    
    def on(self,r,g,b):
        self.set_color(r,g,b)
        
    def off(self):
        self.set_color(0,0,0)
        
led = LED()
led.on(0,0,255)
        
        




