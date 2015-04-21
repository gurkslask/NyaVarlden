__author__ = 'alexander'

from PIL import Image
import os
import sys

def create_tb(infile):
    size = (128, 128)
    outfile = os.path.splitext(infile)[0] + '.thumbnail'
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError as e:
            print('cannot create thumbnail {} \n {}'.format(infile, e))

def check_files():
    for i in os.listdir():
        if os.path.splitext(i)[1] == '.jpg':
            yield i
        else:
            print('Skipped {}'.format(i))
            print('info {}'.format(os.path.splitext(i)))

if __name__ == '__main__':
    a = check_files()
    for i in a:
        create_tb(i)


