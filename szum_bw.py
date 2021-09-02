from PIL import Image
import PIL
import math

def calc_avr(photo: PIL.Image.Image) -> list:
    
    avr_list = []
    w, h = photo.size
    n = w*h

    for i in range(3):
        s = 0
        for j in range(w):
            for k in range(h):
                s += photo.getpixel((j, k))[i]
        avr_list.append(s/n) 

    return avr_list 

def calc_deviation(photo: PIL.Image.Image, avr_list: list) -> list:
    
    dev_list = []

    w, h = photo.size
    n = w*h

    for i in range(3):
        s = 0
        for j in range(w):
            for k in range(h):
                s += (photo.getpixel((j, k))[i] - avr_list[i]) ** 2
        dev_list.append(math.sqrt(s/n)) 
    
    return dev_list

def calc_percent_deviation(dev_list: list, avr_list: list) -> list:

    perc_dev_list = []

    for i in range(3):
        perc_dev_list.append(dev_list[i]/avr_list[i] * 100)

    return perc_dev_list

############################################
#def main(photo: PIL.Image.Image, mode: int) -> list:
def main():

    #wstaw ścieżkę do zdjęcia
    im = Image.open("cropped_images/SD.JPG")
    x,y = im.size

    px = im.convert("RGB")

    results_list = []

    supp_list = []

    avr_supp = calc_avr(px)
    dev_supp = calc_deviation(px, avr_supp)

    supp_list.append(avr_supp)
    supp_list.append(dev_supp)
    supp_list.append(calc_percent_deviation(dev_supp, avr_supp))

    results_list.append(supp_list)

    print(results_list)
    #wyświetlenie i interpretacja wyników

if __name__ == "__main__":
    #main(photo, mode)
    main()

    

        






