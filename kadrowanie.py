from PIL import Image
import PIL
import math

import glob

def openFolder(path):
    for filename in glob.glob(path + '/*.JPG'):
        img=Image.open(filename)

    return img

def find_max_index(t: tuple) -> int:
    max = -1
    max_index = -1
    for idx, val in enumerate(t):
        if(val>max):
            max = val
            max_index = idx
            
    return max_index

def is_dark_red(value: tuple) -> bool:
    if((value[0] > 1.4 * value[1] and value[0] > value[2] * 1.4) and (value[0] > 20 + value[1] and value[0] > value[2] + 20)):
        return True
    else:
        return False

def red_diff(value: tuple) -> bool:
    if(value[0] - 15 > value[1] and value[0] -15 > value[2]):
        return True
    else:
        return False

def is_red(value: tuple) -> bool:
    if((value[0]>=130 and value[1]< 130 and value[2] < 130 and red_diff(value) and find_max_index(value) == 0) or is_dark_red(value)):
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
        p = px.crop((crop_coords[i][0], crop_coords[i][1], crop_coords[i][2], crop_coords[i][3]))
        cropped_images.append(p)
        p.save("crop_pom/pom" + str(i) + ".png")
        
    return cropped_images

def choose_crop_coordinates(lt: list, x: int, y: int, mfw: int, mfh: int) -> tuple:
    
    lt1 = lt
    
    for i in range(4):
            
            xf = i%2
            yf = math.floor(i/2)
            
            lt1[i][0] = xf * (x - mfw) + lt1[i][0]
            lt1[i][1] = yf * (y - mfh) + lt1[i][1]

    #left
    min_hor = 10000
    for i in range(4):
        if(lt1[i][0] < min_hor):
            min_hor = lt1[i][0]
            
    #top
    min_vert = 10000
    for i in range(4):
        if(lt1[i][1] < min_vert):
            min_vert = lt1[i][1]
            
    #right
    max_hor = -1
    for i in range(4):
        if(lt1[i][0] > max_hor):
            max_hor = lt1[i][0]
            
    #down
    max_vert = -1
    for i in range(4):
        if(lt1[i][1] > max_vert):
            max_vert = lt1[i][1]
            
    if(not(min_vert == 10000 or min_hor == 10000 or max_vert == -1 or max_hor == -1 )):
        
        return (min_hor, min_vert, max_hor, max_vert)
    
    else:
        print("Blad wyboru wspolrzednych")
        return (-1, -1, -1, -1)
     

def find_crop_point(img: Image.Image) -> list:
    
    im = img
    
    x, y = im.size
    
    row_points = []

    max1 = 0
    p_max1 = -1

    min = x
    p_min = -1

    max2 = 0
    p_max2 = -1

    #finding stage
    fs = 0

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
        if(fs == 0):
        
            if(value > max1):
                max1 = value
                p_max1 = index
                
            elif(max1 * 0.5 > value and max1 - 10 > value):
          
                fs = 1
                
        #find min
        if(fs == 1):
        
            if(value < min and value != 0):
                min = value
                p_min = index
                
            elif(min * 2 < value and min + 10 < value):
                fs = 2
        
        if(fs == 2):
        #find max2
            if(value > max2):
                max2 = value
                p_max2 = index
            
    if(not (p_max1 == -1 or p_min == -1 or p_max2 == -1)):

        first = -1
        last = 0

        for i in range(x):
            k = im.getpixel((i, p_min))
            
            if(is_red(k)):
                    first = i
                    last = first + min
                    
                
                    
        if(not(first == -1)):
            cpy = p_min
            cpx = first + math.floor((last - first)/2)
            
            cp = [cpx, cpy]
            
            return cp

        else:
            print("Blad znalezienia pierwszego i ostatniego czerwonego piksela w wierszu min")
            return [-1, -1]
    else:
        print("Blad indeksow do znalezienia minimum czerwonego")
        return [-2, -2]  

def main(im: Image.Image):

    if(im):
        #okreslenie o ile wycinek ma byc dalej wyciety od rogu zdjecia planszy
        x, y = im.size

        if(0.6 <= y/x <= 0.706):
        
            mfw = 240
            mfh = 240
        elif(0.706 < y/x <= 0.8):
            mfw = 350
            mfh = 350
        else:
            print("Niepoprawne proporcje zdjęcia")
            return 0 
        
        #przygotowanie wycinkow rogow kadrow
        cropped_images = []
        cropped_images = vertexes_cropped_images(im, mfw, mfh, x, y)
        
        coords_list = []
        
        #znalezienie gdzie jest punkt wyciecia na kazdym obszarze do kontroli kadrowania planszy
        for i in range(4):
            pom = find_crop_point(cropped_images[i])
            if(not(pom[0] == -1 or pom[0] == -2)):
                coords_list.append(pom)
            else:
                return 0
        
        #ustalenie ktore z punktow wyciecia definiuje jak najwiekszy wycinek i na jego podstawie przygtowanie wpolrzednych do kadrowania
        ccc = choose_crop_coordinates(coords_list, x, y, mfw, mfh)
        
        if(not (ccc == (-1, -1, -1, -1))):
            imout = im.crop(ccc)
            
            imout.save("cropped_photo/pokadrowaniu.png")
            
            print("Kadrowanie zakonczone")
            
            return imout
        else:
            print("Niepoprawne kadrowanie")
            return 0
            
    else:
        print("Kadruj - blad: nie wprowadzono poprawnie zdjecia")
        return 0
        
if __name__ == "__main__":
    main(im)

        
        
    


