import cv2 
import pytesseract
from openpyxl import load_workbook

def find_empty_row(sh) -> int:
    
    r = 0
    
    for i in range(4, 1000):
        if(not (sh.cell(row = i, column = 1).value)):
            r = i
            break
    return r

def getFontSize(line: str) -> str:

    if(line[1] == ' '):
        return line[0]
    else:
        return line[:3]

def recognition(n: int) -> float:
    
    tekst = " Praca magisterska rnGC6mmmm"
    OCR1_nr_list = ["6.5", "6", "5.5", "5", "4.5", "4", "3.5", "3"]
    OCR2_nr_list = ["2.7", "2.4", "2.1", "1.8", "1.5", "1.2", "1", "0.8", "0.6"]

    #mode = "OCR1"

    img = cv2.imread("cropped_images/OCR" + str(n) + ".JPG")

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    #print(pytesseract.image_to_string(img, config=custom_config))

    f = open("OCR" + str(n) +"_temp.txt", "w")

    f.write(pytesseract.image_to_string(img, config=custom_config))

    f.close()

    i=0
    label = eval("OCR" + str(n) + "_nr_list")

    with open('OCR' + str(n) + '_temp.txt','r') as file: 
        for line in file:
            if(line[0].isnumeric()):
                #printlabel[i] + tekst)
                #print("line:", line)
                value = label[i] + tekst
                #value = "6.5 Praca magisterska rnGC6mmmm"

                if(value in line):
                    print(getFontSize(line) + " - ok")
                    if(i != len(label) - 1):
                        i += 1
                else:
                    i -= 1
                    break
    if(i<0):
        return 9
    else:
        return label[i]

def main():
    
    wb = load_workbook(filename = 'output.xlsx')
    sheet = wb['5_OCR']
    
    empty_row = find_empty_row(sheet)
    
    min = 10
    
    for i in range(1,3):
        temp = float(recognition(i))
        if(temp < min):
            min = temp
    
    if(min == 9):
        sheet.cell(row = empty_row, column = 1).value = "Nic nie rozpoznano"
    else:
        sheet.cell(row = empty_row, column = 1).value = min

    wb.save('output.xlsx')
    
if __name__ == "__main__":
    main()

