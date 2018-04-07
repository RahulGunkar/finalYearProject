import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import timeit

from PIL import Image

def pil_test():
    cm_hot = mpl.cm.get_cmap('hot')
    img_src = Image.open('output/odm_orthophoto.png').convert('L')
    img_src.thumbnail((512,512))
    im = np.array(img_src)
    im = cm_hot(im)
    im = np.uint8(im * 255)
    im = Image.fromarray(im)
    im.save('ndvi.jpg')

def rgb2gray(rgb):
    return np.dot(rgb[:,:,:3], [0.499, 0.587, 0.114])



t = timeit.timeit(pil_test, number=30)
print('PIL: %s' % t)
