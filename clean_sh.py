from openpyxl import load_workbook

def main():

    wb = load_workbook("output.xlsx")


    for sheet in wb.worksheets:
        for i in range(4, 100):
            for j in range(1, 90):
                
                sheet.cell(row = i, column = j).value = None
                
    wb.save("output.xlsx")
    wb.close()
    
    wb2 = load_workbook("komunikat.xlsx")   
    
    sheet2 = wb2['Arkusz1']   
    
    for i in range(1, 40):
        for j in range(2, 100):
                
            sheet2.cell(row = i, column = j).value = None
    
    wb2.save("komunikat.xlsx")
    wb2.close()
    
if __name__ == "__main__":
    main()