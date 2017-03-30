# coding=utf-8
from PIL import ImageGrab, Image
im= ImageGrab.grabclipboard()
if isinstance(im, Image.Image):
    im.save('tmp.jpg')