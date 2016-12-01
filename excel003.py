#Program for reading and editing a existing work book

import openpyxl
import openpyxl.styles

#loading a workbook
wb = openpyxl.load_workbook('Book1.xlsx')

#printing sheet names
print wb.get_sheet_names()

#selecting a sheet
sheet=wb.get_sheet_by_name('Sheet1')

#Adding data 
sheet['A2']="Bc Roy 123"

# adding fill font/colour 
ft = openpyxl.styles.PatternFill(start_color="ff8080",end_color="ff8080",fill_type='solid')
sheet["A2"].fill=ft

# saving script(DO NOT FORGET TO SAVE)
wb.save('Book1.xlsx')

#reading value from a sheet
print sheet['A2'].value




