import sys
#import rogi 
from PIL import Image
from PIL.ExifTags import TAGS
from openpyxl import load_workbook

#własne skrypty 
import test_rozdzielczosci_bw_mtf
import test_rozdzielczosci_gb
import test_rozdzielczosci_rb
import test_rozdzielczosci_rg

import winietowanie
import dystorsje
import ocr
import szum_bw
import szum_rgb
import rozroznialnosc


def main():
    #https://www.thepythoncode.com/article/extracting-image-metadata-in-python
    
    # path to the image or video
    imagename = "photo/test.jpg"

    # read the image data using PIL
    image = Image.open(imagename)

    # extract EXIF data
    exifdata = image.getexif()
    
    #data = [exifdata[0x0110], exifdata[0xA405], exifdata[0x0100], 
    # exifdata[0x0101], exifdata[0x9202][0]/exifdata[0x9202][1], 
    # exifdata[0x9201][0]/exifdata[0x9201][1], exifdata[0x8827], "-" ]

    wb = load_workbook(filename = 'output.xlsx')
    
    sheet = wb['1_Ustawienia_aparatu']
    
    empty_row = 0
    
    for i in range(4, 1000):
        if(not (sheet.cell(row = i, column = 1).value)):
            empty_row = i
            break
        
    #Model aparatu
    try:
         sheet.cell(row = empty_row, column = 1).value = exifdata[0x0110] 
    except:
         sheet.cell(row = empty_row, column = 1).value = "-"
         
    #Dlugosc ogniskowa
    try:
         sheet.cell(row = empty_row, column = 2).value = exifdata[0xA405] 
    except:
         sheet.cell(row = empty_row, column = 2).value = "-"
         
    #Długość obrazu
    try:
         sheet.cell(row = empty_row, column = 3).value = exifdata[0x0100] 
    except:
         sheet.cell(row = empty_row, column = 3).value = "-"
         
    #Szerokość obrazu
    try:
         sheet.cell(row = empty_row, column = 4).value = exifdata[0x0101] 
    except:
         sheet.cell(row = empty_row, column = 4).value = "-"
         
    #Przyslona
    try:
         sheet.cell(row = empty_row, column = 5).value = exifdata[0x9202][0]/exifdata[0x9202][1] 
    except:
         sheet.cell(row = empty_row, column = 5).value = "-"
         
    #Czas naswietlania
    try:
         sheet.cell(row = empty_row, column = 6).value = exifdata[0x9201][0]/exifdata[0x9201][1] 
    except:
         sheet.cell(row = empty_row, column = 6).value = "-"
         
    #ISO
    try:
         sheet.cell(row = empty_row, column = 7).value = exifdata[0x8827] 
    except:
         sheet.cell(row = empty_row, column = 7).value = "-"
         
    #Model obiektywu
    try:
         sheet.cell(row = empty_row, column = 8).value = exifdata[0xA434] 
    except:
         sheet.cell(row = empty_row, column = 8).value = "-"
    
    """
    for j in range(1,9):
            k = sheet.cell(row = empty_row, column = j).value
            if(not k):
                try:
                    if(data[j-1]):
                        sheet.cell(row = empty_row, column = j).value = data[j-1]
                    else:
                        sheet.cell(row = empty_row, column = j).value = "-"
                except:
                    sheet.cell(row = empty_row, column = j).value = "-"               
    """
                  
    wb.save('output.xlsx')
    
    test_rozdzielczosci_bw_mtf.main()
    test_rozdzielczosci_rg.main()
    test_rozdzielczosci_gb.main()
    test_rozdzielczosci_rb.main()
    winietowanie.main()
    dystorsje.main()
    ocr.main()
    szum_bw.main()
    szum_rgb.main()
    rozroznialnosc.main()
    
if __name__ == "__main__":
    main()