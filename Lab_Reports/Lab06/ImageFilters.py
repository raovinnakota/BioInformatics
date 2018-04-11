# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:44:20 2018

@author: Kerri-Ann Norton
Image Filters
"""

from PIL import Image, ImageEnhance

from matplotlib import pyplot
from numpy import array, dot, dstack, ones, random, uint8, zeros, exp, mgrid, sqrt
from scipy import ndimage 

def pixmapToImage(pixmap, mode='RGB'):
  
  if pixmap.max() > 255:
    pixmap *= 255.0 / pixmap.max()

  pixmap = array(pixmap, uint8)
  img = Image.fromarray(pixmap, mode)
  
  return img
  
  
def imageToPixmapRGB(img):
  
  img2 = img.convert('RGB')
  w, h = img2.size  
  data = img2.getdata()

  pixmap = array(data, float)
  pixmap = pixmap.reshape((h,w,3))
  
  return pixmap


def gammaAdjust(pixmap, gamma=1.0):

  pixmap = array(pixmap, float)/255.0
  pixmap = pixmap ** gamma
  pixmap *= 255
  
  return pixmap


def normalisePixmap(pixmap):
  
  pixmap -= pixmap.min()
  maxVal = pixmap.max()
  
  
  if maxVal > 0:
    pixmap *= 255.0 / maxVal
  
  return pixmap


def clipPixmapValues(pixmap, minimum=0, maximum=255):
  
  pixmap2 = pixmap.copy()
  grey = pixmap2.mean(axis=2)
  
  boolArray = grey < minimum
  indices = boolArray.nonzero()
  pixmap2[indices] = minimum
  
  boolArray = grey > maximum
  indices = boolArray.nonzero()
  pixmap2[indices] = maximum
  
  return pixmap2


def showHistogram(pixmap):

  grey = pixmap.mean(axis=2)
  values = grey.flatten().tolist()
  
  pyplot.hist(values, 256)
  pyplot.show()
  
  
def convolveMatrix2D(pixmap, matrix, mode='reflect'):
  
  matrix = array(matrix)

  if matrix.ndim != 2:
    raise Exception('Convolution matrix must be 2D')

  if pixmap.ndim not in (2,3):
    raise Exception('Pixmap must be 2D or 3D')
  
  if pixmap.ndim == 2:
    pixmap2 = ndimage.convolve(pixmap, matrix, mode=mode)

  else:
    layers = []
    
    for i in range(3):
      layer = ndimage.convolve(pixmap[:,:,i], matrix, mode=mode)
      layers.append(layer)
      
    pixmap2 = dstack(layers)
    
  
  return pixmap2


def sharpenPixmap(pixmap):

  matrix = [[-1,-1,-1],
            [-1, 8,-1],
            [-1,-1,-1]]
  
  grey = pixmap.mean(axis=2)
  
  pixmapEdge = convolveMatrix2D(grey, matrix)
  normalisePixmap(pixmapEdge)
  
  pixmapEdge -= pixmapEdge.mean()
  pixmapEdge = dstack([pixmapEdge, pixmapEdge, pixmapEdge])
  
  pixmapSharp = pixmap + pixmapEdge 
  pixmapSharp = pixmapSharp.clip(0, 255)
  
  return pixmapSharp


def gaussFilter(pixmap, r=2, sigma=1.4):

  x, y = mgrid[-r:r+1, -r:r+1]

  s2 = 2.0 * sigma * sigma
  
  x2 = x * x / s2
  y2 = y * y / s2
  
  matrix = exp( -(x2 + y2))
  matrix /= matrix.sum()
  
  pixmap2 = convolveMatrix2D(pixmap,  matrix)
  
  return pixmap2


def sobelFilter(pixmap):

  matrix = array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])

  grey = pixmap.mean(axis=2)
  edgeX = convolveMatrix2D(grey, matrix)
  edgeY = convolveMatrix2D(grey, matrix.T)
 
  pixmap2 = sqrt(edgeX * edgeX + edgeY * edgeY)
  normalisePixmap(pixmap2) # Put min, max at 0, 255
  return pixmap2 
  
if __name__ == '__main__':  
    # Image adjustments and filters

  img = Image.open('examples/Cells.jpg')

  processObj = ImageEnhance.Contrast(img)
  img2 = processObj.enhance(2.0)
  img2.show()

  processObj = ImageEnhance.Sharpness(img)

  img2Sharp = processObj.enhance(4.0)
  img2Sharp.show()

  imgBlur = processObj.enhance(0.5)
  imgBlur.show()
 
  imgBrighter = ImageEnhance.Brightness(img).enhance(0.5)
  imgDull = ImageEnhance.Color(img).enhance(0.1)


  # Image adjustments and histograms with NumPy

  img = Image.open('examples/Cells.jpg')
  pixmap = imageToPixmapRGB(img)

  showHistogram(pixmap)

  pixmap2 = gammaAdjust(pixmap, 0.5)
  pixmap3 = clipPixmapValues(pixmap2, 0, 145)
  pixmap4 = normalisePixmap(pixmap3)

  pixmapToImage(pixmap4).show()

  # Image filters with NumPy/SciPy

  img = Image.open('examples/Cells.jpg')
  pixmap = imageToPixmapRGB(img)
  
  matrix = [[ 1, 1, 1],
            [ 1, 8, 1],
            [ 1, 1, 1]]

  pixmapBlur = convolveMatrix2D(pixmap, matrix)
  pixmapBlur /= array(matrix).sum()
  
  pixmapToImage(pixmapBlur).show()

  img = Image.open('examples/Cells.jpg')
  imageToPixmapRGB(img)

  pixmap = sharpenPixmap(pixmap)
  pixmapToImage(pixmap).show()

  pixmap = gaussFilter(pixmap)
  pixmapToImage(pixmap).show()

  pixmapGrey = sobelFilter(pixmap)
  pixmapToImage(pixmapGrey, mode='L').show()

  
