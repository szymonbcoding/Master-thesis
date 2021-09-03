from PIL import Image
import PIL
from openpyxl import load_workbook
import math

def convertMmToPx(val, mm, px):
    return math.ceil(val*px/mm)

crop_list = []
save_list = []
labels = []

w34 = 488.889
w23 = 550
h = 366.67

x_crop_difference = 30
y_crop_difference = 51.5


im = Image.open('photo/test.jpg')
x, y = im.size

if(0.63 < y/x < 0.705):
    mode = 23
    w = w23
elif(0.705 <= y/x < 0.79):
    mode = 34
    w = w34
else:
    print("Wrong image resolution.")

label = "BW_RT5"
left_mm = 208.9445
top_mm = 128.355
right_mm = 233.9445
down_mm = 174.835


out = im.crop((math.floor(left_mm*x/w), math.floor(top_mm*y/h), math.floor(right_mm*x/w), math.floor(down_mm*y/h)))
out.save('cropped_images/' + label + '.JPG')