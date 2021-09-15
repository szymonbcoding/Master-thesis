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

def is_red(value: tuple) -> bool:
    if(value[0]>=130 and value[1]<= 130 and value[2] <= 130 and find_max_index(value) == 0):
        return True
    else:
        return False
    
def is_green(value) -> bool:
    if(value[1]>=50 and value[0]<= 150 and value[2] <= 150 and find_max_index(value) == 1):
        return True
    else:
        return False

def openFolder(path) -> Image.Image:
    for filename in glob.glob(path + '/*.JPG'):
        img=Image.open(filename)

    return img

def vertexes_cropped_images(px: Image.Image, mfw: float, mfh: float, x: int, y: int) -> list:

    
    #                   left-top            right-top              left-down             right-down
    crop_coords = [[0, 0, mfw, mfh], [x - mfw, 0, x, mfh ], [0, y - mfh, mfw, y], [x - mfw, y - mfh, x , y]]

    cropped_images = []

    for i in range(4):
        cropped_images.append(px.crop((crop_coords[i][0], crop_coords[i][1], crop_coords[i][2], crop_coords[i][3])))
        
    return cropped_images

def choose_crop_coordinates(lt: list, x: int, y: int, mfw: int, mfh: int) -> tuple:
    #input 
    #list: left-top, right-top, left-down, right-down
    
    
    for i in range(4):
            
            xf = i%2
            yf = math.floor(i/2)
            
            lt[i][0] = xf * (x - mfw) + lt[i][0]
            lt[i][1] = yf * (y - mfh) + lt[i][1]
            
    """
    Rownoznaczny kod, ale mniej czytelny
    for i in range(4):
        for j in range(2):
            f = (i%2, math.floor(i/2))
            
            lt[i][j] = ((j + 1) % 2) * f[0] * (x - mfw) + (j % 2) * f[1] * (y - mfh) + lt[i][j]
    
    """
    #left
    min_hor = 10000
    for i in range(4):
        if(lt[i][0] < min_hor):
            min_hor = lt[i][0]
            
    #top
    min_vert = 10000
    for i in range(4):
        if(lt[i][1] < min_vert):
            min_vert = lt[i][1]
            
    #right
    max_hor = -1
    for i in range(4):
        if(lt[i][0] < max_hor):
            max_hor = lt[i][0]
            
    #down
    max_vert = -1
    for i in range(4):
        if(lt[i][1] < max_vert):
            max_vert = lt[i][1]
            
    if(not(min_vert == 10000 or min_hor == 10000 or max_vert == -1 or max_hor == -1 )):
        
        return (min_hor, min_vert, max_hor, max_vert)
    
    else:
        print("Blad wyboru wspolrzednych")
        return (-1, -1, -1, -1)
     

def find_crop_point(n: int, img: Image.Image):
    
    im = img
    
    x, y = im.size
    
    row_points = []
    """
    print("srodek:", im.getpixel((4, 5)))

    print("czerwony:", im.getpixel((30, 35)))


    #print("krawedz:", im.getpixel((65, 58)))

    #print("uśrednione tło:", im.getpixel((70, 43)))

    print("tło:", im.getpixel((63, 65)))
    """

    max1 = 0
    p_max1 = -1

    min = x
    p_min = -1

    max2 = 0
    p_max2 = -1

    find_min_on = False
    find_max2_on = False

    for i in range(y):
        liczba = 0 
        for j in range(x):
            k = im.getpixel((j,i))
            
            if(is_red(k)):
                liczba += 1
            if(j == x - 1):
                row_points.append(liczba)

    #find crop_point
    for index, value in enumerate(row_points):
        #find max1
        if(value > max1 and not find_min_on):
            max1 = value
            p_max1 = index
            
        elif(max1 * 0.5 > value and max1 - 10 > value):
            find_min_on = True
        
        #find min
        if(find_min_on and value < min):
            min = value
            p_min = index
            
        elif(find_min_on and min * 2 < value and min + 10 < value):
            find_min_on = False
            find_max2_on = True
        
        #find max2
        if(find_max2_on and value > max2):
            max2 = value
            p_max2 = index
            
    if(not (p_max1 == -1 or p_min == -1 or p_max2 == -1)):
        print("MAX1 - value:", max1, "index:", p_max1)
        print("MIN - value:", min, "index:", p_min)
        print("MAX2 - value:", max2, "index:", p_max2)

        first = -1
        last = -1

        first_flag = True

        for i in range(x):
            k = im.getpixel((i, p_min))
            
            if(is_red(k)):
                if(first_flag):
                    first = i
                    first_flag = False
                elif(first + min - 2 < i and not first_flag):
                    last = i
                    
        if(not(first == -1 or last == -1)):
            cpy = p_min
            cpx = first + math.floor((last - first)/2)
        
            print("Punkt wyciecia:")
            print(cpx, cpy)
            
            return (cpx, cpy)

        else:
            print("Blad znalezienia pierwszego i ostatniego czerwonego piksela w wierszu min")
            return (-1, -1)
    else:
        print("Blad indeksow do znalezienia minimum czerwonego")
        return (-2, -2)
    
    
    """
    for index, value in enumerate(row_points):
        print(index, value)
    """     

def main():
    
    im = Image.open("folder/s1.JPG")

    #okreslenie o ile wycinek ma byc dalej wyciety od rogu zdjecia planszy
    x, y = im.size
    w_f = -1
    h_f = -1
    if(0.63 < y/x < 0.705):
        w_f = 1/40
        h_f = 1/26
    elif(0.705 <= y/x < 0.79):
        w_f = 1/40
        h_f = 1/30
    else:
        print("Nieobslugiwana proporcja obrazu.")
    
    
    mfw = math.floor(x * w_f)
    mfh = math.floor(y * h_f)
    
    #przygotowanie wycinkow rogow kadrow
    cropped_images = []
    cropped_images = vertexes_cropped_images(im, mfw, mfh, x, y)
    
    tuple_list = []
    
    #znalezienie gdzie jest punkt wyciecia na kazdym obszarze do kontroli kadrowania planszy
    for i in range(4):
        tuple_list.append(find_crop_point(i, cropped_images[i]))
    
    #ustalenie ktore z punktow wyciecia definiuje jak najwiekszy wycinek i na jego podstawie przygtowanie wpolrzednych do kadrowania
    im.crop(choose_crop_coordinates(tuple_list, x, y, mfw, mfh)).save("photo/pokadrowaniu.png")

if __name__ == "__main__":
    main()

        
        
    


