from PIL import Image
import PIL
import math

def find_odd_pixel(v: int, avr1: float) -> bool:
    
    if(abs(v - avr1) > 50):
        return True
    else:
        return False

def calc_avr(photo: PIL.Image.Image) -> float:
    
    w, h = photo.size
    n = w*h

    s = 0

    for j in range(w):
        for k in range(h):
            s += photo.getpixel((j, k))

    return (s/n)

def winiet(avr_v: float, avr_c: float) -> bool:

    if(abs(avr_v-avr_c) > 10):
        return True
    else:
        return False

############################################
def main():

    image_list = []

    for i in range(1, 6):
    
        image_list.append(Image.open("cropped_images/BW_RT" + str(i) + ".JPG").convert("L"))

    sv = 0

    for i in range(4):
        sv += calc_avr(image_list[i])
    
    avr_vertexes = sv/4

    avr_center = calc_avr(image_list[4])

    print("Srednia wartosc piksela na wierzcholkach planszy:", avr_vertexes)
    print("Srednia wartosc piksela na srodku planszy:", avr_center)

    if(winiet(avr_vertexes, avr_center)):
        print("Winietowanie widoczne")
    else:
        print("Brak winietowania")

if __name__ == "__main__":
    #main(photo, mode)
    main()