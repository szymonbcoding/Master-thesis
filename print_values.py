from PIL import Image, ImageOps
import PIL
import math

def find_max_index(t: tuple) -> int:
    max = -1
    max_index = -1
    for idx, val in enumerate(t):
        if(val>max):
            max = val
            max_index = idx
            
    return max_index

def main():

    label = "pom0.png"
    
    im = Image.open(label).convert("RGB")
    x, y = im.size
    
    print(im.getpixel((77, 37)))
    
   

if __name__ == "__main__":
    main()