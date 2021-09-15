from PIL import Image
import PIL
import math

import glob

def find_max_index(t: tuple) -> int:
    max = -1
    max_index = -1
    for idx, val in enumerate(t):
        if(val>max):
            max = val
            max_index = idx
            
    return max_index

def is_red(value):
    if(value[0]>=130 and value[1]<= 130 and value[2] <= 130 and find_max_index(value) == 0):
        return True
    else:
        return False
    
def is_green(value):
    if(value[1]>=50 and value[0]<= 150 and value[2] <= 150 and find_max_index(value) == 1):
        return True
    else:
        return False

def openFolder(path):
    for filename in glob.glob(path + '/*.JPG'):
        img=Image.open(filename)

    return img

im = Image.open("folder/s1.JPG")

x, y = im.size

row_points = []
"""
print("srodek:", im.getpixel((4, 5)))

print("czerwony:", im.getpixel((30, 35)))


#print("krawedz:", im.getpixel((65, 58)))

#print("uśrednione tło:", im.getpixel((70, 43)))

print("tło:", im.getpixel((63, 65)))
"""

for i in range(y):
    liczba = 0 
    for j in range(x):
        k = im.getpixel((j,i))
        
        if(is_red(k)):
            liczba += 1
        if(j == x - 1):
            row_points.append(liczba)

for index, value in enumerate(row_points):
    print(index, value)
        
        
        
        
        
    


