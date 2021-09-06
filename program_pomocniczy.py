from PIL import Image
import PIL
from openpyxl import load_workbook
import math

w34 = 488.889
w23 = 550
h = 366.67

im = Image.open('photo/test.JPG')
x, y = im.size

if(0.63 < y/x < 0.705):
    mode = 23
    w = w23
elif(0.705 <= y/x < 0.79):
    mode = 34
    w = w34
else:
    print("Nieobslugiwana proporcja obrazu.")

left = 517
top = 308.67
right = 542
down = 355.17

label = "BW_RT4"

im.crop((left * x/w, top * y/h, right * x/w, down * y/h)).save('cropped_images/' + label + '.JPG')






    

    


    
