from PIL import Image
import PIL
from openpyxl import load_workbook
import math

w34 = 488.889
w23 = 550
h = 366.67

im = Image.open('photo/test.JPG')
x, y = im.size

wb = load_workbook(filename = 'coordinates_v2.xlsx')

if(0.63 < y/x < 0.705):
    mode = 23
    w = w23
    sheet = wb['23']
elif(0.705 <= y/x < 0.79):
    mode = 34
    w = w34
    sheet = wb['34']
    
else:
    print("Nieobslugiwana proporcja obrazu.")

label = "RG_RT"

pointer = -1

for i in range(2, 19):
    if(label in sheet.cell(row = i, column = 1).value):
        pointer = i


if(pointer > 1):

    left = round(sheet.cell(row = pointer, column = 2).value, 4)
    top = round(sheet.cell(row = pointer, column = 3).value, 4)
    right = round(sheet.cell(row = pointer, column = 4).value, 4)
    down = round(sheet.cell(row = pointer, column = 5).value, 4)
    
    
    dleft = 1.5
    dtop = -1
    
    dright = dleft
    ddown = dtop



    im.crop(((left + dleft) * x/w, (top + dtop) * y/h, (right + dright) * x/w, (down + ddown) * y/h)).save('cropped_images/' + label + '.JPG')
else:
    print("Blad")





    

    


    
