from PIL import Image
import PIL
import math

def is_red(value):
    if(value[0]>=100 and value[1]<= 100 and value[2] <= 100):
        return True
    else:
        return False

def is_black(value):
    tolerancy = 50
    for i in range(3):
        if(value[i]>tolerancy):
            return False
    return True

def correct_frame(photos):
    
    counter = 0

    for photo in photos:
        w, h = photo.size

        for i in range(w):
            for j in range(h):
                v = photo.getpixel((i, j))
                if(is_red(v)):
                    counter += 1
    
    if(counter>=0):
        return True
    else:
        return False

#program liczy czerwone i czarne piksele w rogach kadru
#róg = kwadrat 5x5
#jeśli suma jest >= 20, to kadrowanie jest poprawne

def main():

    im = Image.open("photo/test.jpg")
    x,y = im.size

    px = im.convert("RGB")

    crop_coords = [[0, 0, 5, 5], [x - 5, 0, x, 5 ], [0, y - 5, 5, y], [x - 5, y - 5, x , y]]

    cropped_images = []

    for i in range(4):
        cropped_images.append(px.crop((crop_coords[i][0], crop_coords[i][1], crop_coords[i][2], crop_coords[i][3])))


    if(correct_frame(cropped_images)):
        print("Poprawne kadrowanie")
        return True
    else:
        print("Niepoprawne kadrowanie")
        return False

if __name__ == "__main__":
    main()
