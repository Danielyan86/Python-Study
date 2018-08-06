
import Image

im = Image.open("oxygen.png")
print im.format, im.mode, im.size

w,h=im.size

print im.getpixel((0,h//2))

print ''.join([chr(im.getpixel((i,h//2))[0]) for i in range(0,w,7)])

print ''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))