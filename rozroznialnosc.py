from PIL import Image
import PIL
import math

#DO ZMIANY, JEŚLI ARKUSZ SIĘ ZMIENI
x_mm = 118
y_mm = 58

square_side_mm = 20

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

############################################
#def main(photo: PIL.Image.Image, mode: int) -> list:
def main():

    #wstaw ścieżkę do zdjęcia
    im = Image.open("cropped_images/CD2.JPG")
    x,y = im.size

    square_side_px = math.floor(x * square_side_mm / x_mm)

    px = im.convert("L")

    v_quarter = math.floor(y/4)

    #obliczanie średniej wartości pikseli pierwszego wiersza
    sum1 = 0
    for i in range(x):
            sum1 += px.getpixel((i, 0))

    avr1 = sum1/x

    h_pointer = -1

    for i in range(x):

        j = px.getpixel((i, v_quarter))

        if(find_odd_pixel(j, avr1)):
            h_pointer = i + 0.25 * square_side_px
            break
    
    crop_coords = []

    for i in range(10):

        supp_list = []

        if(i < 5):
            q = 1
        elif(i >= 5):
            q = 3

        #left, top, right, down
        supp_list.append(h_pointer + (i % 5) * square_side_px)
        supp_list.append(q * v_quarter - 0.2 * square_side_px)
        supp_list.append(h_pointer + ((i % 5) + 0.5) * square_side_px)
        supp_list.append(q * v_quarter + 0.2 * square_side_px)

        crop_coords.append(supp_list)
    

    cropped_images = []

    for i in range(10):
        cropped_images.append(px.crop((crop_coords[i][0], crop_coords[i][1], crop_coords[i][2], crop_coords[i][3])))
        #cropped_images[i].save('bw/' + str(i) + '.JPG')

    labels = ["black", "white"]

    for i in range(10):

        if(i < 5):
            print("Black" + str(i))
        elif(i >= 5):
            print("White" + str(i - 5))

        a = calc_avr(cropped_images[i])

        print("Average:", a)
        print("")

if __name__ == "__main__":
    #main(photo, mode)
    main()