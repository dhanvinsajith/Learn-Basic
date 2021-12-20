from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter


wb = load_workbook('SampleData.xlsx')



'''
ws = wb.active #gets active sheet
print(ws['D23'].value)
ws['C23'] = 'Morgan' #modifying cell value
print(wb.sheetnames) #prints all sheets
# wb.create_sheet('Test') #creating sheets
# print(wb.sheetnames)
'''



'''
ws = wb['TestSheet'] #accessing particular sheet
ws.title = 'TestSheet' #change sheet name
ws.append([50, 75, 24, 67, 81, 90])
ws.append([21, 9, 10, 42, 64, 128])
'''



'''
#accessing a certain series of cells
ws = wb['Office']
for row in range(1, 11):
    for col in range(1, 6):
        char = get_column_letter(col)
        print(ws[char + str(row)].value)
#changing values of a certain series of cells
ws = wb['TestSheet']
for row in range(3, 17):
    for col in range(1, 7):
        char = get_column_letter(col)
        ws[char + str(row)] = char + str(row)
'''



'''
# wb.create_sheet('TestingFunctions')
ws = wb['TestingFunctions']
ws.merge_cells("A1:E1")
ws.unmerge_cells('A1:E1') #there will be no data in unmerged cells because they were merged previously
ws.merge_cells('C8:E11') #merges in rectangular region
ws.insert_rows(10)
ws.insert_rows(10)
ws.delete_rows(10) #deletes one of two added
ws.insert_cols(3) #adds C column
ws.insert_cols(4) 
ws.delete_cols(4) #deletes empty C column
'''


ws = wb['TestingFunctions']
ws.move_range('F1:F19', rows = 2, cols = 3) #moves 3 to the right and 2 to the bottom

wb.save('SampleData.xlsx')