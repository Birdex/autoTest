# -*- coding: utf-8 -*-

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((400, 600))
im.save('thumb.jpg', 'JPEG')