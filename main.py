from ST7735S import ST7735S
from bmp import bmp
import time
import lcd_gfx

d = ST7735S()
d.reset()
d.begin()
d._bground = 0xffff
d.fill_screen(d._bground)

d.set_rotation(0)
bmp('flower64x48.bmp',d,10,10,1)

d.set_rotation(1)
bmp('flower64x48.bmp',d,10,10,1)

d.set_rotation(2)
bmp('flower64x48.bmp',d,10,10,1)

d.set_rotation(3)
bmp('flower64x48.bmp',d,10,10,1)

d._color = 0
d.set_rotation(0)
d.p_string(10,10,'Hello World')

d._color = 0xf100
d.set_rotation(1)
d.p_string(10,10,'Hello World')

d._color = 0x07e0
d.set_rotation(2)
d.p_string(10,10,'Hello World')

d._color = 0x001f
d.set_rotation(3)
d.p_string(10,10,'Hello World')

time.sleep(5)
d.set_rotation(3)
bmp('flower160x128.bmp',d,0,0,1)

time.sleep(5)
x = int(d._width/2)
y = int(d._height/2)
r = int(min(x,y)/2)
d.fill_screen(d.rgb_to_565(255,255,255))
color = d.rgb_to_565(0,36,125)
lcd_gfx.drawfillCircle(x,y,r,d,color)
r = int(r*2/3)
color = d.rgb_to_565(255,255,255)
lcd_gfx.drawfillCircle(x,y,r,d,color)
r = int(r/2)
color = d.rgb_to_565(206,17,38)
lcd_gfx.drawfillCircle(x,y,r,d,color)
