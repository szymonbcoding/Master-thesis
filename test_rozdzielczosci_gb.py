from PIL import Image
import PIL
import math


def main():
    
    #maksymalna wysokosc testu rozdzielczosci[mm]
    MAX = 20
    #wysokosc calej planszy testowej [mm]
    h = 366.67

    #zaladowanie całego obrazu planszy
    im1 = Image.open('photo/test.jpg')

    x_all, y_all = im1.size

    if(0.63 < y_all/x_all < 0.705):
        w = 550
    elif(0.705 <= y_all/x_all < 0.79):
        w = 488.889
    else:
        print("Błędna rozdzielczość planszy.")

    #przeliczenie 20mm (bok testu rozdzielczosci) na piksele
    px_20mm = math.floor(y_all * MAX/h)

    pict = Image.open('cropped_images/GB_RT.JPG')

    im2 = pict.convert("RGB")

    #rozdzielczosc wycinka
    x, y = im2.size

    #print("Blue:", im2.getpixel((22, 30)))
    
    #print("Red:", im2.getpixel((37, 42)))

    #PETLA TESTU ROZDZIELCZOSCI POZIOMEJ

    #inicjalizacja zmiennych pomocniczych
    hor_res = 0
    v_pointer = -1

    for i in range(math.floor(1.5 * px_20mm)):
        #resetowanie zmiennych
        hor_edges = 0
        hor_flag = False

        for j in range (0, x):

            if((im2.getpixel((j,i))[1] >= 60) and (im2.getpixel((j,i))[2] <= 60) and not hor_flag):

                hor_flag = True
            
            elif((im2.getpixel((j,i))[2] >= 60) and (im2.getpixel((j,i))[1] <= 60) and hor_flag):
                
                hor_flag = False
                hor_edges += 1

                if(v_pointer == -1):
                    v_pointer = i + px_20mm
            
            #sprawdzanie czy program naliczyl 5 zbocz 
            if(hor_edges>=5):
                hor_res += 1
                break

    print("hor_res: " + str(hor_res))
    #stosunek poprawnych wierszy (najlepszy mozliwy wynik = 1, najgorszy mozliwy wynik = 0)
    p_row_found = hor_res/px_20mm

    #2 - (1.8 * 0) = 2 (najgorszy wynik)
    #2 - (1.8 * 1) = 0.2 (najlepszy wynik)
    h_mm_resolution = 2 - (1.8 * p_row_found)

    real_h_px_resolution = math.floor(w/h_mm_resolution)

    print("Rzeczywista pozioma rozdzielczosc: " + str(real_h_px_resolution))
    print("Maksymalna mozliwa pozioma rozdzielczosc " + str(math.floor(w/0.2)))

    #PETLA TESTU ROZDZIELCZOSCI PIONOWEJ

    ver_res = 0

    for i in range(x):
        #resetowanie zmiennych
        ver_edges = 0
        ver_flag = False

        for j in range (v_pointer, y):

            if((im2.getpixel((i,j))[2] >= 60) and (im2.getpixel((i,j))[1] <= 60) and not ver_flag):

                ver_flag = True
            
            elif((im2.getpixel((i,j))[1] >= 60) and (im2.getpixel((i,j))[2] <= 60) and ver_flag):
                
                ver_flag = False
                ver_edges += 1
                
            #sprawdzanie czy wykryto przynajmniej 5 zbocz
            if(ver_edges>=5):
                ver_res += 1
                break

    print("ver_res: " + str(ver_res))
    #stosunek poprawnych kolumn (najlepszy wynik = 1, najgorszy wynik = 0)
    p_col_found = ver_res/px_20mm

    #2 - (1.8 * 0) = 2 (najgorszy wynik)
    #2 - (1.8 * 1) = 0.2 (najlepszy wynik)
    v_mm_resolution = 2 - (1.8 * p_col_found)

    real_v_px_resolution = math.floor(h/v_mm_resolution)

    print("Rzeczywista pionowa rozdzielczosc: " + str(real_v_px_resolution))
    print("Najwyzsza mozliwa pionowa rozdzielczosc " + str(math.floor(h/0.2)))


if __name__ == "__main__":
    main()
            
