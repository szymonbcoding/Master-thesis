import cv2 
import pytesseract

def getFontSize(line: str) -> str:

    if(line[1] == ' '):
        return line[0]
    else:
        return line[:3]

def main():
    
    tekst = " Praca magisterska rnGC6mmmm"
    OCR1_nr_list = ["6.5", "6", "5.5", "5", "4.5", "4", "3.5", "3"]
    OCR2_nr_list = ["2.7", "2.4", "2.1", "1.8", "1.5", "1.2", "1", "0.8", "0.6"]

    result = -1
    #mode = "OCR1"
    mode = "OCR2"

    img = cv2.imread("cropped_images/" + mode + ".JPG")

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    #print(pytesseract.image_to_string(img, config=custom_config))

    f = open("ocr_txt_files/" + mode +"_temp.txt", "w")

    f.write(pytesseract.image_to_string(img, config=custom_config))

    f.close()

    i=0
    label = eval(mode + "_nr_list")

    with open('ocr_txt_files/' + mode + '_temp.txt','r') as file: 
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
        print("Nic nie rozpoznało")
    else:
        print("result:", getFontSize(label[i] + tekst))

if __name__ == "__main__":
    main()

