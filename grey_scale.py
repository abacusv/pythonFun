import sys
import os
import numpy as np
import cv2
''' opencv2 opens a image file and creates a vector of type (x,y,[r,g,b]).
    To convert the image into grey scale we need to store only one value
    of the rgb. The best way to do so is to store in format (x,y). The
    color value at (x,y) should be avg of [r,g,b] value
'''
def grey_scale(image):
    return (image.sum(2)/3).astype(np.uint8)

exts = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg', 
    '.jpe', '.jp2', '.tiff', '.tif', '.png', '.JPG']

def main(imagepath):
    if not os.path.exists(imagepath):
        print "Error: File not found"
        return

    '''some native checking and converting steps '''
    print "Loading image {}".format(imagepath)
    dirpath = os.path.dirname(imagepath)
    fname = os.path.basename(imagepath)
    name, ext = os.path.splitext(fname)
    if ext not in exts:
        print "Unsupported file type"
        return
    ''' read the image file '''
    img = cv2.imread(imagepath)
    out_img = grey_scale(img)
    out_path = os.path.join(dirpath, "{}_{}.{}".format(name, "grey", ext))
    cv2.imwrite(out_path, out_img)


if __name__ == "__main__":
        main(sys.argv[1])


