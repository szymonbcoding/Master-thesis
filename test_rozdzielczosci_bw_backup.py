from PIL import Image
import PIL
import math

def contrast(vmax: int, vmin: int) -> float:
    return ((vmax - vmin)/(vmax + vmin))

def mtf(cf: float, c0: float) -> float:
    return (100 * cf/c0)

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
    px_20mm = math.ceil(y_all * MAX/h)

    #zaladowanie obrazu w wersji monochromatycznej
    im2 = Image.open('cropped_images/BW_RT4.JPG').convert("L")

    #rozdzielczosc wycinka
    x, y = im2.size

    #PETLA TESTU ROZDZIELCZOSCI POZIOMEJ

    #inicjalizacja zmiennych pomocniczych
    hor_res = 0
    v_pointer = -1
    h_pointer = -1

    mtf_row0 = True
    h_mtf_pointer = -1
    h_vw_0 = -1
    h_vb_0 = 256
    
    for i in range(math.floor(1.5 * px_20mm)):
        #resetowanie zmiennych
        hor_edges = 0
        hor_flag = False

        for j in range(x):

            if(v_pointer != -1):
                #sprawdzanie wartości najmniejszej i największej dla pierwszego wiersza testu rozdzielczości
                if(mtf_row0):
                    if(im2.getpixel((j,i)) > h_vw_0):
                        h_vw_0 = im2.getpixel((j,i))
                    elif(im2.getpixel((j,i)) < h_vb_0):
                        h_vb_0 = im2.getpixel((j,i))

            if(im2.getpixel((j,i)) >= 120 and not hor_flag):

                hor_flag = True
            
            elif(im2.getpixel((j,i)) <= 60 and hor_flag):

                hor_flag = False
                hor_edges += 1

                if(v_pointer == -1):
                    
                    h_pointer = j
                    v_pointer = i + px_20mm
                    
            #sprawdzanie czy program naliczyl 5 zbocz 
            if(hor_edges>=5):
                hor_res += 1
                mtf_row0 = False
                h_mtf_pointer = i
                break

    print("hor_res: " + str(hor_res))
    #stosunek poprawnych wierszy (najlepszy mozliwy wynik = 1, najgorszy mozliwy wynik = 0)
    p_row_found = hor_res/px_20mm
    

    #2 - (1.8 * 0) = 2 (najgorszy wynik)
    #2 - (1.8 * 1) = 0.2 (najlepszy wynik)
    h_mm_resolution = 2 - (1.8 * p_row_found)
    print("h_mm_resolution:", h_mm_resolution)

    real_h_px_resolution = math.floor(w/h_mm_resolution)

    print("Rzeczywista pozioma rozdzielczosc: " + str(real_h_px_resolution))
    print("Maksymalna mozliwa pozioma rozdzielczosc " + str(math.floor(w/0.2)))

    #MTF
    
    #sprawdzenie o ile spadł kontrast w ostatnim wierszu gdzie rozróżnił
    pom = []
    
    h_vw_f = -1
    h_vb_f = 256

    length_last_row_px = 10 * h_mm_resolution * x_all / w
    print("length_last_row_px:", length_last_row_px)

    for i in range(h_pointer, math.floor(h_pointer + 0.8 *length_last_row_px)):
        #print(im2.getpixel((i, h_mtf_pointer)))
        #print(im2.getpixel((i, v_pointer - px_20mm)))
        pom.append(im2.getpixel((i, v_pointer - 0.75 * px_20mm)))
        if(im2.getpixel((i, h_mtf_pointer)) > h_vw_f):
            h_vw_f = im2.getpixel((i, h_mtf_pointer))
        elif(im2.getpixel((i, h_mtf_pointer)) < h_vb_f):
            h_vb_f = im2.getpixel((i, h_mtf_pointer))

    print("Avr:", sum(pom)/len(pom))

    h_mtf_result = mtf(contrast(h_vw_f, h_vb_f), contrast(h_vw_0, h_vb_0))
    print("h_vw_0:", h_vw_0, "h_vb_0:", h_vb_0, "h_vw_f:", h_vw_f, "h_vb_f:", h_vb_f)
    print("h_mtf_result:", h_mtf_result)
    #PETLA TESTU ROZDZIELCZOSCI PIONOWEJ

    ver_res = 0
    v_pointer = -1
    h_pointer = -1

    mtf_col0 = True
    v_mtf_pointer = -1
    v_vw_0 = -1
    v_vb_0 = 256

    for i in range(x):
        #resetowanie zmiennych
        ver_edges = 0
        ver_flag = False

        for j in range (v_pointer, y):

            if(v_pointer != -1):
                #sprawdzanie wartości najmniejszej i największej dla pierwszego wiersza testu rozdzielczości
                if(mtf_col0):
                    if(im2.getpixel((i,j)) > v_vw_0):
                        v_vw_0 = im2.getpixel((i,j))
                    elif(im2.getpixel((i,j)) < v_vb_0):
                        v_vb_0 = im2.getpixel((i,j))

            if(im2.getpixel((i,j)) <= 60 and not ver_flag):

                ver_flag = True
            
            elif(im2.getpixel((i,j)) >= 120 and ver_flag):
                
                ver_flag = False
                ver_edges += 1
            
            if(v_pointer == -1):
                    
                    v_pointer = j

            #sprawdzanie czy wykryto przynajmniej 5 zbocz
            if(ver_edges>=5):
                ver_res += 1
                mtf_col0 = False
                v_mtf_pointer = j
                h_pointer = i
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

    #MTF
    
    #sprawdzenie o ile spadł kontrast w ostatnim wierszu gdzie rozróżnił

    v_vw_f = -1
    v_vb_f = 256

    length_last_col_px = 10 * v_mm_resolution * y_all / h
    print("length_last_col_px:", length_last_col_px)

    for j in range(math.floor(v_mtf_pointer - 0.8 * length_last_col_px), v_mtf_pointer):
        print(im2.getpixel((h_pointer, j)))
        if(im2.getpixel((h_pointer, j)) > v_vw_f):
            v_vw_f = im2.getpixel((h_pointer, j))
        elif(im2.getpixel((h_pointer, j)) < v_vb_f):
            v_vb_f = im2.getpixel((h_pointer, j))

    v_mtf_result = mtf(contrast(v_vw_f, v_vb_f), contrast(v_vw_0, v_vb_0))
    print("v_vw_0:", v_vw_0, "v_vb_0:", v_vb_0, "v_vw_f:", v_vw_f, "v_vb_f:", v_vb_f)
    print("v_mtf_result:", v_mtf_result)

if __name__ == "__main__":
    main()
            
