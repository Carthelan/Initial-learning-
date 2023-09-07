import csv
import tkinter
from collections import defaultdict



with open(r'C:\Users\Klill\Desktop\Test.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') 
    dict = {}
    for row in reader:
        date = row[0]
        data = row[1]
        if date not in dict:
            dict[date] = {data: 1}
        elif data not in dict[date]:
            dict[date][data] = 1
        else: 
            dict[date][data] += 1
    print(dict)    
        

        
#tkinter to make a gui 
