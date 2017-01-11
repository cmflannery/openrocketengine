#!/usr/bin/env python
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
# ascii_art.py
__author__ = "Cameron Flannery"
__copyright__ = "Copyright 2017"
__credits__ = ["Cameron Flannery"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Cameron Flannery"
__email__ = "cmflannery@ucsd.edu"
__status__ = "Development"


class ascii_text(object):
    """ ascii_text creates an object that can be used to display ascii text on\
    the console """
    def __init__(self, text):
        self.ShowText = text

    def display_text(self):
        fontsize = 10
        try:
            font = ImageFont.truetype('Arial.ttf', fontsize)  # load the font
        except IOError:
            font = ImageFont.truetype('arialbd.ttf', fontsize)
        size = font.getsize(self.ShowText)  # calc the size of text in pixels
        image = Image.new('1', size, 1)  # create a b/w image
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), self.ShowText, font=font)  # render text to bitmap
        for rownum in range(size[1]):
            # scan the bitmap:
            # print ' ' for black pixel and
            # print '#' for white one
            line = []
            for colnum in range(size[0]):
                if image.getpixel((colnum, rownum)):
                    line.append(' '),
                else:
                    line.append('#'),
            print ''.join(line)


class ascii_image(object):
    """ ascii_image creates an object that can be used to display an image to
    the console """
    def __init__(self, fname):
        self.fname = fname

    def display_image(self):
        with open(self.fname, 'r') as fin:
            print fin.read()
