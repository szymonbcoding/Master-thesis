from PIL import Image
import PIL
import math

crop_list = []

#resolution tests coordinates
w_ratio34 = 244.4445
w_ratio23 = 275
h = 183.335

w_difference = w_ratio23 - w_ratio34
x_crop_difference = 30
y_crop_difference = 51.5

im = Image.open('2021-05-02.jpg')
x, y = im.size

if(0.63 < y/x < 0.705):
    mode = 23
elif(0.705 <= y/x < 0.79):
    mode = 34
else:
    print("Wrong image resolution.")

if(mode == 34):

    w = w_ratio34

    x2 = math.ceil((239.5 - w_difference)/w * x)

    x3 = math.ceil((239.5 - w_difference)/w * x) 

    x5 = math.ceil((133.5 - w_difference)/w * x)

elif(mode == 23):

    w = w_ratio23

    x2 = math.ceil(239.5/w * x)

    x3 = math.ceil(239.5/w * x)

    x5 = math.ceil(133.5/w * x)
    
x1 = math.ceil(4.5/w * x)
y1 = math.ceil(4.5/h * y)

y2 = math.ceil(4.5/h * y)

y3 = math.ceil(126.335/h * y)

x4 = math.ceil(4.5/w * x)
y4 = math.ceil(126.335/h * y)

y5 = math.ceil(65.415/h * y)

print(x5)

for i in range(1,6):
    crop_list.append(im.crop((eval("x"+ str(i)), eval("y"+ str(i)), eval("x"+ str(i))+x_crop_difference/w*x, eval("y"+ str(i)) + y_crop_difference/h*y)))
    crop_list[i-1].save('resolution/resolution_crop' + str(i) + '.jpg')

#im1 = im.crop((x1,y1,x1+x_crop_difference,x1+y_crop_difference))
#im2 = im.crop((x2,y2,x2-x_crop_difference,y2+))
    