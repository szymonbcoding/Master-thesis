from PIL import Image, ImageOps
import PIL
import math


def main():

    im = Image.open('cropped_images/in.JPG')
    mono = ImageOps.grayscale(im)
    x, y = mono.size
    
    for i in range(y):
        print("")
        for j in range(x):
            print(mono.getpixel((j, i)), end=' ')
   

if __name__ == "__main__":
    main()