import csv
import tkinter
from collections import defaultdict



with open(r'C:\Users\Klill\Desktop\Test.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    dictionary = defaultdict(list)
    keyList = []
    for row in reader:
        date = row[0]
        data = row[1]
        dictionary[date].append(data)
        
        
            
        

#now read the dictionary to spit out the days, the values, and how many times they appear 
    for key in dictionary:
        print(dictionary.values())
        

        
#tkinter to make a gui 
