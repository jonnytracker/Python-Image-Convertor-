from pickletools import optimize
from PIL import Image
import PIL
import os
import glob


import pathlib


path = pathlib.Path(r"D:\3D\textures")


def compress_image(directory=False, quality=75):

    #if directory not empty
    if directory:
        os.chdir(directory)

    
    #get all the folder list in the variable files
    files = os.listdir()

    images = [file for file in files if file.endswith(('png'))]

    for image in images:
        print(image)
       
        f, e = os.path.splitext(image)

        savefile = f + ".jpg"

        img = Image.open(image)
      
        rgb = img.convert('RGB')
      
        

        rgb.save(savefile,optimize= True, quality=quality)


compress_image(path)
