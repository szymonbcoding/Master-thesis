from PIL import Image
import PIL
import math

from openpyxl import load_workbook

def find_empty_row(sh) -> int:
    
    r = 0
    
    for i in range(4, 1000):
        if(not (sh.cell(row = i, column = 1).value)):
            r = i
            break
    return r

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

    if(avr_c-avr_v > 10):
        return True
    else:
        return False

############################################
def main():

    wb = load_workbook(filename = 'output.xlsx')
    sheet = wb['3_Winietowanie']
    
    empty_row = find_empty_row(sheet)
    
    image_list = []

    for i in range(1, 6):
    
        image_list.append(Image.open("cropped_images/BW_RT" + str(i) + ".JPG").convert("L"))

    sv = 0

    for i in range(4):
        sv += calc_avr(image_list[i])
    
    avr_vertexes = sv/4

    avr_center = calc_avr(image_list[4])

    print("Srednia wartosc piksela na wierzcholkach planszy:", avr_vertexes)
    sheet.cell(row = empty_row, column = 1).value = round(avr_vertexes, 1)
    
    print("Srednia wartosc piksela na srodku planszy:", avr_center)
    sheet.cell(row = empty_row, column = 2).value = round(avr_center, 1)
    
    message = "Blad"
    
    if(winiet(avr_vertexes, avr_center)):
        message = "Winietowanie widoczne"
    else:
        message = "Brak winietowania"
        
    sheet.cell(row = empty_row, column = 3).value = message
    
    wb.save('output.xlsx')

if __name__ == "__main__":
    #main(photo, mode)
    main()