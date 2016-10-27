# MicroPython_ST7735S

Last update added support for a cheap 128x128 TFT display.
offset - offsets the display by that number of pixels horizontally and vertically
c_mode - Swaps around Blue and Red in the 565 colour packet. It seems some displays swap these.

Sample usage
```python
import ST7735

# height defaults to 160
ST7735.ST7735_TFTHEIGHT = 128

# move image 3 pixels across and down
# RGB is reversed = c_mode fixes that
d = ST7735.ST7735(offset=3, c_mode='BGR')
d.reset()
d.begin()
d._bground = 0xffff
d.fill_screen(d._bground)
```


