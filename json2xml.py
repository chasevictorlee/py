#!/usr/bin/env python

import json
import xlwt


wb = xlwt.Workbook()
ws = wb.add_sheet('student')

with open("student.txt", 'r') as f:
    data = json.load(f)

data = sorted(data.items(), key = lambda d:d[0])

i = -1
j = 0

for row in data:
    i = i + 1
    ws.write(i, 0, row[0])
    for col in row[1]:  
        j = j + 1
        ws.write(i, j, col)
    j = 0

wb.save('student.xls')
