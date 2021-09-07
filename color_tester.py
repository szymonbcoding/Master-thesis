from PIL import Image
import PIL
from openpyxl import load_workbook
import math


label = "RG_RT"
x_pointer = 29
y_pointer = 201

im = Image.open('cropped_images/' + label + '.JPG')
x, y = im.size

if(x_pointer < x and y_pointer < y):
    print(im.getpixel((x_pointer, y_pointer)))
else:
    print("Niepoprawne wspolrzedne piksela")
