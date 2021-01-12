import glob
import sys
import cv2
import numpy as np
from PIL import Image
import os
from skimage import io

if len(sys.argv) > 1:
    root_dir = sys.argv[1]
else:
    print("Use target path as argument")
    quit()
    
if (root_dir[-1] != "\\"):
    root_dir = root_dir+"\\"

for filename in glob.iglob(root_dir + '**/**', recursive=True):
    try:
        if filename.endswith('.jpg'):
            myimg = cv2.imread(filename)
            avg_color_per_row = np.average(myimg, axis=0)
            avg_color = np.average(avg_color_per_row, axis=0)
            array = np.array(avg_color, dtype=np.uint8)
            print(str(filename)+" "+str(array))
            new_image = Image.new('RGB', (4,4), tuple(reversed(array.tolist())))
            os.remove(filename)
            new_image.save(filename)
    except:
        print(str(filename)+": ERROR")
        input("Press Enter to continue...")
        continue