from PIL import Image
import PIL
import math

#jeśli żadna ze składowych nie różni się od średniej
#o więcej niż 30 to zwróć False
#inaczej zwróć True

def differences(p: list, avr: float) -> bool:
    for i in range(n):
        if(abs(avr - p[i]>30):
            return True
    return False

#sprawdzanie czy w danym wierszu
#ponad połowa pikseli różni się od wzorca

def oddRow(r: list, avr1: float) -> bool:
    result = 0

    for i in (len(r)):
        if(differences(i, avr1)):
            result += 1

    if(result/len(r)>0.5):
        return True
    else:
        return False

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
    im = Image.open("")
    x,y = im.size

    px = im.convert("RGB")

    #obliczanie średniej wartości pikseli pierwszego wiersza
    sum1 = 0
    for i in range(x):
        for j in range(3):
            sum1 += px.getpixel((x, 0))[j]

    #dzielnik razy 3, bo 3 składowe - RGB
    avr1 = sum1/(3*x)

    nr_odd_row = -1
    nr_odd_col = -1

    for i in range(1, y):
        row = []
        for j in range(x):
            row.append(px.getpixel((j,i)))
    
        #jeśli w danym wierszu więcej niż połowa pikseli
        #różni się od średniej pierwszego wiersza
        #to zaczynamy operację
        if(oddRow(row, avr1)):
            nr_odd_row = i
            break

    if(nr_odd_row == -1):
        print("Błąd. Nie wykryto wiersza charaktersytycznego.")

    for i in range(x):
        if(differences(px.getpixel((i, nr_odd_row)), avr1)):
            nr_odd_col = i
            break

    #dodamy margines błędu (dodanie 3 do współrzędnych
    #pktu początkowego)

    nr_odd_col += 3
    nr_ood_row += 3    

    a = poziomy bok prostokąta
    b = pionowy bok prostokąta
    #nie pamiętam czy a = b

    crop_coords = []

    #n = liczba prostokątów
    #współrzędne w pikselach

    for i in (n):
        supp_list = []

        supp_list.append(nr_odd_row + i * a)
        supp_list.append(nr_odd_col)
        supp_list.append(nr_odd_row + a/2 + i * a)
        supp_list.append(nr_odd_col + b/2)

        crop_coords.append(supp_list)

    #te prostokąty chyba zakręcają (nie są w jednej linii)
    #trzeba dodać drugą pętle po tej pierwszej z innymi
    #parametrami 

    #cropowanie obrazów
    cropped_images = []
 
    for i in (n):
        cropped_images.append(im.crop((crop_coords[i][0], crop_coords[i][1], crop_coords[i][2], crop_coords[i][3])))

    results_lists = []

    for i in cropped_images:
        supp_list = []

        avr_supp = calc_avr(i)
        dev_supp = calc_deviation(i, avr_supp)

        supp_list.append(avr_supp)
        supp_list.append(dev_supp)
        supp_list.append(calc_percent_deviation(dev_supp, avr_supp))

        results_lists.append(supp_list)

    print(results_list)
    #wyświetlenie i interpretacja wyników

if __name__ == "__main__":
    #main(photo, mode)
    main()

    

        






